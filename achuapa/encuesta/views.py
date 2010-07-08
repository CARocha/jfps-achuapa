from django.http import Http404, HttpResponse
from encuesta.models import *
from decorators import session_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
	
def inicio(request):
    if request.method == 'POST':
        form = AchuapaForm(request.POST)
        if form.is_valid():
            cooperativa = form.cleaned_data['cooperativa']
            ano = form.cleaned_data['ano']
            departamento = form.cleaned_data['departamento']
            comunidad = form.cleaned_data['comunidad']
            socio = form.cleaned_data['socio']
            dueno = form.cleaned_data['dueno']
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
