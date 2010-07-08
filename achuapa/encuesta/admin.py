from django.contrib import admin
from lugar.models import Municipio
from encuesta.models import *
from django.contrib.contenttypes import generic
   
class DatosInline(generic.GenericStackedInline):
	model = DatosGenerales
	max_num = 1
	
class OrganizacionInline(generic.GenericStackedInline):
    model = Organizacion
    max_num = 1
    
class MigracionInline(generic.GenericTabularInline):
    model = Migracion
    extra = 1
    max_num = 6
    
class TenenciaInline(generic.GenericTabularInline):
    model = Tenencia
    extra = 1
    max_num = 1
    
class TierraInline(generic.GenericTabularInline):
    model = Tierra
    extra = 1
    max_num = 7
    
class ExistenciaArbolesInline(generic.GenericTabularInline):
    model = ExistenciaArboles
    extra = 1
    max_num = 1
    
class ReforestacionInline(generic.GenericTabularInline):
    model = Reforestacion
    extra = 1
    max_num = 9
    
class FincaProduccionInline(generic.GenericTabularInline):
    model = FincaProduccion
    extra = 1
    max_num = None
    
class CultivosFincaInline(generic.GenericTabularInline):
    model = CultivosFinca
    extra = 1
    max_num = None

class IngresoFamiliarInline(generic.GenericTabularInline):
    model = IngresoFamiliar
    extra = 1
    max_num = None

class OtrosIngresosInline(generic.GenericTabularInline):
    model = OtrosIngresos
    extra = 1
    max_num = 4
    
class TipoCasaInline(generic.GenericTabularInline):
    model = TipoCasa
    extra = 1
    max_num = 1
    
class DetalleCasaInline(generic.GenericTabularInline):
    model = DetalleCasa
    extra = 1
    max_num = 1
    
class PropiedadesInline(generic.GenericTabularInline):
    model = Propiedades
    extra = 1
    max_num = 8
    
class HerramientasInline(generic.GenericTabularInline):
    model = Herramientas
    extra = 1
    max_num = 9
    
class TransporteInline(generic.GenericTabularInline):
    model = Transporte
    extra = 1
    max_num = 6
    
class AhorroInline(generic.GenericTabularInline):
    model = Ahorro
    extra = 1
    max_num = 6
    
class CreditoInline(generic.GenericTabularInline):
    model = Credito
    extra = 1
    max_num = 1
    
class EducacionInline(generic.GenericTabularInline):
    model = Educacion
    extra = 1
    max_num = 6
    
class NoEducacionInline(generic.GenericTabularInline):
    model = NoEducacion
    extra = 1
    max_num = 4
    
class SaludInline(generic.GenericTabularInline):
    model = Salud
    extra = 1
    max_num = 6
    
class AguaInline(generic.GenericTabularInline):
    model = Agua
    extra = 1
    max_num = 6
    
class SeguridadInline(generic.GenericTabularInline):
    model = Seguridad
    extra = 1
    max_num = None
    
class EncuestaAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [DatosInline, OrganizacionInline,
            MigracionInline, TenenciaInline, 
            TierraInline, ExistenciaArbolesInline, 
            ReforestacionInline, FincaProduccionInline, 
            CultivosFincaInline, IngresoFamiliarInline, 
            OtrosIngresosInline, TipoCasaInline, 
            DetalleCasaInline, PropiedadesInline, 
            HerramientasInline, TransporteInline, 
            AhorroInline, CreditoInline, EducacionInline, 
            NoEducacionInline, SaludInline, 
            AguaInline, SeguridadInline]
    
    list_display = ['nombre_socios', 'comunidades', 'municipios']
    list_filter = ['fecha']
    date_hierarchy = 'fecha'
    search_fields = ['datos__nombre','datos__comunidad__nombre']



admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Recolector)
admin.site.register(Beneficios)
admin.site.register(PorqueMiembro)
admin.site.register(UsoTierra)
admin.site.register(Maderable)
admin.site.register(Forrajero)
admin.site.register(Energetico)
admin.site.register(Frutal)
admin.site.register(Actividades)
admin.site.register(Nativos)
admin.site.register(NoNativos)
admin.site.register(Animales)
admin.site.register(Producto)
admin.site.register(Cultivos)
admin.site.register(Rubros)
admin.site.register(Fuentes)
admin.site.register(Equipos)
admin.site.register(Infraestructuras)
admin.site.register(NombreHerramienta)
admin.site.register(NombreTransporte)
admin.site.register(AhorroPregunta)
admin.site.register(DaCredito)
admin.site.register(OcupaCredito)
admin.site.register(Alimentos)
admin.site.register(Piso)
admin.site.register(Techo)
