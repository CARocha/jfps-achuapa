from django.http import Http404, HttpResponse
from encuesta.models import *
from decorators import session_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from datetime import date
from django.utils import simplejson
from forms import *
from django.views.generic.simple import direct_to_template
from lugar.models import *

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
            params['cooperativa'] = request.session['cooperativa']

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
#        if request.session['duenio']:
#            params['tenencia__dueno'] = request.session['duenio']

        return Encuesta.objects.filter(**params)

def index(request):
	return render_to_response('base.html',context_instance=RequestContext(request))
	
def inicio(request):
    if request.method == 'GET':
        mensaje = None
        form = AchuapaForm(request.GET)
        if form.is_valid():
            try:
                cooperativa = Cooperativa.objects.get(id=form.cleaned_data['cooperativa'])
            except:
                cooperativa = None
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            try:
                municipio = Municipio.objects.get(id=form.cleaned_data['municipio']) 
            except:
                municipio = None
            try:
                comunidad = Comunidad.objects.get(id=form.cleaned_data['comunidad'])
                
            except:
                comunidad = None
            try:
                socio = Datosgenerales.objects.get(id=form.cleaned__data['socio'])
            except:
                socio = None
            request.session['municipio'] = municipio 
            request.session['comunidad'] = comunidad
            request.session['socio'] = socio
            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
#        else:
#            mensaje = "Formulario con errores"
#            dict = {'form': form, 'mensaje': mensaje,'user': request.user}
#            return direct_to_template(request, 'achuapa/inicio.html', dict)
    else:
        form = AchuapaForm()
        mensaje = ":P"
    dict = {'form': form,'user': request.user}
    return direct_to_template(request, 'achuapa/inicio.html', dict)

@session_required
def familia(request):
    '''Tabla de familias(migracion)'''
    a = _queryset_filtrado
    socios = a.filter(migracion__edades=1).count()
    return render_to_response('achuapa/familia.html',{'socios':socios})

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
    
# Vistas para obtener los municipios, comunidades, socio, etc..

def get_municipios(request, departamento):
    municipios = Municipio.objects.filter(departamento = departamento)
    lista = [(municipio.id, municipio.nombre) for municipio in municipios]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

def get_comunidad(request, municipio):
    comunidades = Comunidad.objects.filter(municipio = municipio )
    lista = [(comunidad.id, comunidad.nombre) for comunidad in comunidades]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
    
def get_socio(request, comunidad):
    socios = DatosGenerales.objects.filter(comunidad = comunidad )
    lista = [(socio.id, socio.nombre) for socio in socios]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
