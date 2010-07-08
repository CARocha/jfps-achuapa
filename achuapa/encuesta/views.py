from django.http import Http404, HttpResponse
from encuesta.models import *
from decorators import session_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from datetime import date

def _queryset_filtrado(request):
    '''metodo para obtener el queryset de encuesta 
    segun los filtros del formulario que son pasados
    por la variable de sesion'''
    fecha = date(int(request.session['ano']), 1, 1)
    #diccionario de parametros del queryset
    params = {}
    if request.session['ano']:
        params['fecha__gt'] = fecha 
        if request.session['cooperativa']:
            params['coop'] = request.session['cooperativa']

        if request.session['departamento']:
            #incluye municipio y comunidad
            if request.session['municipio']:
                if request.session['comunidad']:
                    params['datos__comunidad'] = request.session['comunidad']
                else:
                    params['datos__comunidad__municipio'] = request.session['municipio']
            else:
                params['datos__comunidad__municipio__departamento'] = request.session['departamento']

        if request.session['socio']:
            params['organizacion__desde__socio'] = request.session['socio']
        if request.session['duenio']:
            params['tenencia__dueno'] = request.session['duenio']

        return Encuesta.objects.filter(**params)

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
	
def inicio(request):
    if request.method == 'POST':
        form = AchuapaForm(request.POST)
        if form.is_valid():
            request.session['cooperativa'] = form.cleaned_data['cooperativa']
            request.session['ano'] = form.cleaned_data['ano']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['comunidad'] = form.cleaned_data['comunidad']
            request.session['socio'] = form.cleaned_data['socio']
            request.session['dueno'] = form.cleaned_data['dueno']
            request.session['activo'] = True
        else:
            render_to_response('encuesta/inicio.html', {'form': form, 
                'mensaje': 'Formulario con errores'})
    else:
        form = AchuapaForm()
        render_to_response('encuesta/inicio.html', {'form': form})

@session_required
def familia(request):
    '''Tabla de familias(migracion)'''
    pass

@session_required
def organizacion(request):
    '''tabla de organizacion'''
    pass

@session_required
def fincas(request):
    '''Tabla de fincas'''
    pass

@session_required
def arboles(request):
    '''Tabla de arboles'''
    pass

@session_required
def ingresos(request):
    '''tabla de ingresos'''
    pass

@session_required
def bienes(request):
    '''tabla de bienes'''
    pass

@session_required
def equipos(request):
    '''tabla de equipos'''
    pass

@session_required
def ahorro_credito(request):
    ''' ahorro y credito'''
    pass

@session_required
def servicios(request):
    '''servicios'''
    pass

@session_required
def salud(request):
    '''salud'''
    pass

@session_required
def agua(request):
    '''Agua'''
    pass

@session_required
def luz(request):
    '''Tabla de acceso a energia electrica'''
    pass

@session_required
def seguridad_alimentaria(request):
    '''Seguridad Alimentaria'''
    pass
