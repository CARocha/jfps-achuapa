# -*- coding: UTF-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from django.core.exceptions import ViewDoesNotExist

from encuesta.models import *
from decorators import session_required
from datetime import date
from forms import *
from lugar.models import *
from decimal import Decimal
from utils import grafos


def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'encuesta.views'))
    
def _queryset_filtrado(request):
    '''metodo para obtener el queryset de encuesta 
    segun los filtros del formulario que son pasados
    por la variable de sesion'''
    anio = int(request.session['fecha'])
    #diccionario de parametros del queryset
    params = {}
    if 'fecha' in request.session:
        params['fecha__year'] = anio 
        if 'cooperativa' in request.session:
            params['datos__cooperativa'] = request.session['cooperativa']

        if 'departamento' in request.session:
            #incluye municipio y comunidad
            if request.session['municipio']:
                if 'comunidad' in request.session:
                    params['datos__comunidad'] = request.session['comunidad']
                else:
                    params['datos__comunidad__municipio'] = request.session['municipio']
            else:
                params['datos__comunidad__municipio__departamento'] = request.session['departamento']

        elif 'socio' in request.session:
            params['organizacion__socio'] = request.session['socio']
        #if 'duenio' in  request.session:
        #    params['tenencia__dueno'] = request.session['duenio']
        
        unvalid_keys = []
        for key in params:
            if not params[key]:
                unvalid_keys.append(key)
        
        for key in unvalid_keys:
            del params[key]

        return Encuesta.objects.filter(**params)

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
	
def inicio(request):
    if request.method == 'POST':
        mensaje = None
        form = AchuapaForm(request.POST)
        if form.is_valid():
            try:
                cooperativa = Datosgenerales.objects.get(id=form.cleaned_data['cooperativa'])
            except:
                cooperativa = None
            request.session['cooperativa'] = cooperativa
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
    a = _queryset_filtrado(request)
    #TODO: columnas totales                         
    hombre_adulto = a.filter(migracion__edades = 1).aggregate(Sum('migracion__total_familia'))
    mujeres_adulto = a.filter(migracion__edades = 2).aggregate(Sum('migracion__total_familia'))
    hombre_adolecentes = a.filter(migracion__edades = 3).aggregate(Sum('migracion__total_familia'))
    mujeres_adolecentes = a.filter(migracion__edades = 4).aggregate(Sum('migracion__total_familia'))
    nino = a.filter(migracion__edades = 5).aggregate(Sum('migracion__total_familia'))
    nina = a.filter(migracion__edades = 6).aggregate(Sum('migracion__total_familia'))
#    prueba = hombre_adulto + mujeres_adulto + hombre_adolecentes + mujeres_adolecentes + nino + nina
    #prueba de lista
    a = _queryset_filtrado(request)
    total={}
    nada=[]
    for i in range(1,7):
        total['carlos'] = a.filter(migracion__edades=i).aggregate(carlos=Sum('migracion__total_familia'),alberto=Sum('migracion__viven_casa'),rocha=Sum('migracion__viven_fuera'))
        nada.append(dict.copy(total))
        
    
    print total
#    #TODO: columnas que viven en casa
    hombre_adulto_viven = _queryset_filtrado(request).filter(migracion__edades = 1).aggregate(Sum('migracion__viven_casa'))
    mujeres_adulto_viven = _queryset_filtrado(request).filter(migracion__edades = 2).aggregate(Sum('migracion__viven_casa'))
    hombre_adolecentes_viven =_queryset_filtrado(request).filter(migracion__edades = 3).aggregate(Sum('migracion__viven_casa'))
    mujeres_adolecentes_viven = _queryset_filtrado(request).filter(migracion__edades = 4).aggregate(Sum('migracion__viven_casa'))
    nino_viven = _queryset_filtrado(request).filter(migracion__edades = 5).aggregate(Sum('migracion__viven_casa'))
    nina_viven = _queryset_filtrado(request).filter(migracion__edades = 6).aggregate(Sum('migracion__viven_casa'))
    
    
#    prueba = _queryset_filtrado(request).filter(migracion__edades=1).aggregate(Sum('migracion__total_familia'))
#    print prueba
    return render_to_response('achuapa/familia.html',locals(),
                              context_instance=RequestContext(request))

@session_required
def organizacion(request):
    '''tabla de organizacion'''
    pass

@session_required
def fincas(request):
    '''Tabla de fincas'''

    tabla = {}
    totales = {}
    consulta = _queryset_filtrado(request)

    totales['numero'] = consulta.aggregate(numero=Count('tierra__uso_tierra'))['numero'] 
    totales['porcentaje_num'] = 100
    totales['manzanas'] = consulta.aggregate(area=Sum('tierra__areas'))['area']
    totales['porcentaje_mz'] = 100


    for uso in UsoTierra.objects.exclude(id=1):
        key = slugify(uso.nombre).replace('-', '_')
        query = consulta.filter(tierra__uso_tierra = uso)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, totales['numero'])
        manzanas = query.aggregate(area = Sum('tierra__areas'))['area']
        porcentaje_mz = saca_porcentajes(manzanas, totales['manzanas'])
        tabla[key] = {'numero': numero, 'porcentaje_num': porcentaje_num,
                      'manzanas': manzanas, 'porcentaje_mz': porcentaje_mz}

    
    return render_to_response('achuapa/fincas.html', 
                              {'tabla':tabla, 'totales': totales},
                              context_instance=RequestContext(request))

def fincas_grafos(request, tipo):
    '''Tipo puede ser: tenencia, solares, propietario'''
    consulta = _queryset_filtrado(request)
    #CHOICE_TENENCIA, CHOICE_DUENO
    data = [] 
    legends = []
    if tipo == 'tenencia':
        for opcion in CHOICE_TENENCIA:
            data.append(consulta.filter(tenencia__parcela=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends, 
                'Tenencia de las parcelas', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'solares':
        for opcion in CHOICE_TENENCIA:
            data.append(consulta.filter(tenencia__solar=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends, 
                'Tenencia de los solares', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'propietario':
        for opcion in CHOICE_DUENO:
            data.append(consulta.filter(tenencia__dueno=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends, 
                'Dueño de propiedad', return_json = True,
                type = grafos.PIE_CHART_3D)
    else:
        raise Http404

@session_required
def arboles(request):
    '''Tabla de arboles'''
    pass

@session_required
def animales(request):
    '''Los animales y la produccion'''
    consulta = _queryset_filtrado(request)
    tabla = {}
    totales = {}

    totales['numero'] = consulta.aggregate(numero=Count('fincaproduccion__animales'))['numero'] 
    totales['porcentaje_num'] = 100
    totales['animales'] = consulta.aggregate(cantidad=Sum('fincaproduccion__cantidad'))['cantidad']
    totales['porcentaje_animal'] = 100

    for animal in Animales.objects.all():
        key = slugify(animal.nombre).replace('-', '_')
        query = consulta.filter(fincaproduccion__animales = animal)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, totales['numero'])
        animales = query.aggregate(cantidad = Sum('fincaproduccion__animales'))['cantidad']
        porcentaje_animal = saca_porcentajes(animales, totales['animales'])
        tabla[key] = {'numero': numero, 'porcentaje_num': porcentaje_num,
                      'animales': animales, 'porcentaje_animal': porcentaje_animal}

    
    return render_to_response('achuapa/animales.html', 
                              {'tabla':tabla, 'totales': totales},
                              context_instance=RequestContext(request))

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
    #ahorro
    consulta = _queryset_filtrado(request)
    tabla_ahorro = {}
    totales_ahorro = {}

    totales_ahorro['numero'] = consulta.aggregate(numero=Count('ahorro__ahorro'))['numero'] 
    totales_ahorro['porcentaje_num'] = 100

    columnas_ahorro = [opcion[1] for opcion in CHOICE_AHORRO]

    for pregunta in AhorroPregunta.objects.all():
        key = slugify(pregunta.nombre).replace('-', '_')
        query = consulta.filter(ahorro__ahorro = pregunta)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, totales_ahorro['numero'])
        #formato key: [numero, porcentaje, respuestas....]
        tabla_ahorro[key] = [numero, porcentaje_num]
        for opcion in CHOICE_AHORRO:
            subquery = consulta.filter(ahorro__ahorro = pregunta, ahorro__respuesta = opcion[0]).count()
            subkey = slugify(opcion[1]).replace('-', '_')
            tabla_ahorro[key].append(subquery)

    #credito
    tabla_credito= {}
    totales_credito= {}

    totales_credito['numero'] = consulta.aggregate(numero=Count('credito'))['numero'] 
    totales_credito['porcentaje_num'] = 100

    recibe = consulta.filter(credito__recibe = 1).count()
    menos = consulta.filter(credito__desde = 1).count()
    mas = consulta.filter(credito__desde = 2).count()
    al_dia = consulta.filter(credito__dia= 1).count()
              
    tabla_credito['recibe'] = [recibe, saca_porcentajes(recibe, totales_credito['numero'])]
    tabla_credito['menos'] = [menos, saca_porcentajes(menos, totales_credito['numero'])] 
    tabla_credito['mas'] = [mas, saca_porcentajes(mas, totales_credito['numero'])] 
    tabla_credito['al_dia'] = [al_dia, saca_porcentajes(al_dia, totales_credito['numero'])] 

    dicc = {'tabla_ahorro':tabla_ahorro, 'columnas_ahorro': columnas_ahorro, 
            'totales_ahorro': totales_ahorro, 'tabla_credito': tabla_credito}

    return render_to_response('achuapa/ahorro_credito.html', dicc,
                              context_instance=RequestContext(request))

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

#TODO: completar esto
VALID_VIEWS = {
        'familia': familia,
        'seguridad_alimentaria': seguridad_alimentaria,
        'luz': luz,
        'fincas': fincas,
        'animales': animales,
        'ahorro_credito': ahorro_credito,
        }

def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores_cero = [] #lista para anotar los indices en los que da cero el porcentaje
    for i in range(len(values)):
        porcentaje = (float(values[i])/total)*100
        values[i] = "%.2f" % porcentaje + '%' 
    return values

def saca_porcentajes(dato, total):
    return (dato/float(total)) * 100
