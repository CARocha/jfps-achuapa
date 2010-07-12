from django.conf.urls.defaults import *
from django.conf import settings
from models import Encuesta
 
info = {
         'queryset': Encuesta.objects.all(),
}

urlpatterns = patterns('encuesta.views',
    (r'^index/$', 'index'),
    (r'^consultar/$', 'inicio'),
    (r'^ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    
   
)
