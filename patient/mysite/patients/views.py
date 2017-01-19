from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
import json
from django.core.serializers.json import DjangoJSONEncoder
import numpy as np
from utils import *
from django.db.models import Max
from django.http import JsonResponse
# Create your views here.
def index(request):

    inputs=condition()
    ids=["Minimum PSA","Maximum PSA","Minimum prostate_vol",
         "Maximum prostate_vol","Minimum lesion_size",
         "Maximum lesion_size","Minimum sector","Maximum sector",
         "Minimum PIRADS_score","Maximum PIRADS_score",
         "Minimum GLEASON_score","Maximum GLEASON_score"]
    list=zip(inputs,ids)
    patient_list=Patient.objects.all()
    attr=attrs()
    attr=attr[1:]
    context={'list':list,'number':len(patient_list),'attr':attr}

    return render(request,'patients/index.html',context)


def loadData(request):
    if request.method=="GET" and request.is_ajax:
        patient_list=Patient.objects.all()
        result=[]
        attr=attrs()
        for i in patient_list:
            d=dict()
            d[attr[0]]=i.patient_ID
            d[attr[1]]=i.PSA
            d[attr[2]]=i.prostate_vol
            d[attr[3]]=i.lesion_size
            d[attr[4]]=i.sector
            d[attr[5]]=i.PIRADS_score
            d[attr[6]]=i.GLEASON_score
            result.append(d)
        d=dict()
        d['data']=result
        result=json.dumps(d,cls=DjangoJSONEncoder)
        return HttpResponse(result)
def AddNewPatient(request):
    print request.POST
    attr=attrs()[1:]
    data=[]
    maxid=Patient.objects.all().aggregate(Max('patient_ID'))
    maxid=maxid['patient_ID__max']
    print maxid
    if request.method=="POST" and request.is_ajax:
        for i in range(len(attr)):
            if not request.POST[attr[i]]:
                return HttpResponse(json.dumps({"success":False,'message':'missing value'}))
            data.append(float(request.POST[attr[i]]))

        p=Patient(patient_ID=maxid+1,PSA=data[0],prostate_vol=data[1],lesion_size=data[2],
                  sector=data[3],PIRADS_score=data[4],GLEASON_score=data[5])
        p.save()
        return JsonResponse({"success":True})

def filter(request):
    print "get--------------",request.GET
    conditions=condition()
    values=request.GET
    if request.method=="GET" and request.is_ajax():
        patient_list=Patient.objects.all()
        print len(patient_list)
        if conditions[0] in values:
            if request.GET[conditions[0]]:
                patient_list=patient_list.filter(PSA__gte=float(request.GET[conditions[0]]))
        if conditions[1] in values:
            if request.GET[conditions[1]]:
                patient_list=patient_list.filter(PSA__lte=float(request.GET[conditions[1]]))
        if conditions[2] in values:
            if request.GET[conditions[2]]:
                patient_list=patient_list.filter(prostate_vol__gte=float(request.GET[conditions[2]]))
        if conditions[3] in values:
            if request.GET[conditions[3]]:
                patient_list=patient_list.filter(prostate_vol__lte=float(request.GET[conditions[3]]))
        if conditions[4] in values:
            if request.GET[conditions[4]]:
                patient_list=patient_list.filter(lesion_size__gte=float(request.GET[conditions[4]]))
        if conditions[5] in values:
            if request.GET[conditions[5]]:
                patient_list=patient_list.filter(lesion_size__lte=float(request.GET[conditions[5]]))
        if conditions[6] in values:
            if request.GET[conditions[6]]:
                patient_list=patient_list.filter(sector__gte=float(request.GET[conditions[6]]))
        if conditions[7] in values:
            if request.GET[conditions[7]]:
                patient_list=patient_list.filter(sector__lte=float(request.GET[conditions[7]]))
        if conditions[8] in values:
            if request.GET[conditions[8]]:
                patient_list=patient_list.filter(PIRADS_score__gte=float(request.GET[conditions[8]]))
        if conditions[9] in values:
            if request.GET[conditions[9]]:
                patient_list=patient_list.filter(PIRADS_score__lte=float(request.GET[conditions[9]]))
        if conditions[10] in values:
            if request.GET[conditions[10]]:
                patient_list=patient_list.filter(GLEASON_score__gte=float(request.GET[conditions[10]]))
        if conditions[11] in values:
            if request.GET[conditions[11]]:
                patient_list=patient_list.filter(GLEASON_score__lte=float(request.GET[conditions[11]]))
        result=[]
        number=len(patient_list)
        attr=attrs()
        for i in patient_list:
            d=dict()
            d[attr[0]]=i.patient_ID
            d[attr[1]]=i.PSA
            d[attr[2]]=i.prostate_vol
            d[attr[3]]=i.lesion_size
            d[attr[4]]=i.sector
            d[attr[5]]=i.PIRADS_score
            d[attr[6]]=i.GLEASON_score
            result.append(d)
        d=dict()
        d['data']=result
        d['number']=number
        result=json.dumps(d,cls=DjangoJSONEncoder)
        return HttpResponse(result)
def GetChart(request):
    if request.method=="GET" and request.is_ajax:
        attr=attrs()
        patient_list=Patient.objects.all()
        result=[]
        for i in attr[1:]:
            data=[]
            for j in patient_list:
                data.append(float(j.getValue(i)))
            (his,bins)=np.histogram(data)
            hist=his.tolist()
            bins=bins.tolist()
            bins=bins[1:]
            result.append([[bins[i],hist[i]] for i in range(len(bins))])
        result=json.dumps(result,cls=DjangoJSONEncoder)
        return HttpResponse(result)







