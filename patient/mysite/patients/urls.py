from django.conf.urls import url

from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^loadData/$',views.loadData,name='loadData'),
    url(r'^filter/$',views.filter,name='filter'),
    url(r'^GetChart/$',views.GetChart,name='GetChart'),
    url(r'^AddNewPatient/$',views.AddNewPatient,name='AddNewPatient')
]