 # -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from encuesta.models import *
from lugar.models import *

date_inputformats=['%d.%m.%Y','%d/%m/%Y','%Y-%m-%d']

class AchuapaForm(forms.Form):
    cooperativa = forms.ModelsChoiceField(required = False, 
            queryset=Cooperativa.objects.all())
    ano = forms.ChoiceField('Años', choices=(2010, 2011))
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
            required=False, empty_label="Todos los Departamento")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comunidad = forms.CharField(widget = forms.Select, required=False)
    socio = forms.CharField(widget = forms.Select, required=False)
    dueno = forms.CharField('Dueño', widget = forms.select, required=False)
