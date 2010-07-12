 # -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from encuesta.models import *
from lugar.models import *

date_inputformats=['%d.%m.%Y','%d/%m/%Y','%Y-%m-%d']
ANOS_CHOICES = ((2010,'2010'),(2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'))

class AchuapaForm(forms.Form):
    cooperativa = forms.ModelChoiceField(required = False, 
            queryset=Cooperativa.objects.all())
    fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
            required=False, empty_label="Todos los Departamento")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comunidad = forms.CharField(widget = forms.Select, required=False)
    socio = forms.CharField(widget = forms.Select, required=False)
#    dueno = forms.CharField('Dueño', widget = forms.select, required=False)
