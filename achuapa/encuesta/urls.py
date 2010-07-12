import os
from django.conf.urls.defaults import *
from django.conf import settings
from models import Encuesta
 
info = {
         'queryset': Encuesta.objects.all(),
}

urlpatterns = patterns('encuesta.views',
    (r'^index/$', 'inicio'),
    (r'^familia/$', 'familia'),
#    (r'^inicio/$', 'inicio'),
    (r'^index/ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^index/ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    (r'^ajax/socio/(?P<comunidad>\d+)/$', 'get_socio'),
    
   
)
