from __future__ import unicode_literals

from django.db import models
from utils import *
# Create your models here.
class Patient(models.Model):
    patient_ID=models.IntegerField(primary_key=True)
    PSA=models.DecimalField(max_digits=10, decimal_places=1)
    prostate_vol=models.DecimalField(max_digits=10, decimal_places=1)
    lesion_size=models.DecimalField(max_digits=10, decimal_places=1)
    sector=models.IntegerField()
    PIRADS_score=models.IntegerField()
    GLEASON_score=models.IntegerField()
    att=attrs()
    def getValue(self,attr):
        if attr==self.att[0]:
            return self.patient_ID
        elif attr==self.att[1]:
            return self.PSA
        elif attr==self.att[2]:
            return self.prostate_vol
        elif attr==self.att[3]:
            return self.lesion_size
        elif attr==self.att[4]:
            return self.sector
        elif attr==self.att[5]:
            return self.PIRADS_score
        elif attr==self.att[6]:
            return self.GLEASON_score