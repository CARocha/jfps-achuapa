from django.contrib import admin
from lugar.models import Municipio
from encuesta.models import DatosGenerales, Organizacion, Migracion, Tenencia, Tierra, ExistenciaArboles, Reforestacion, FincaProduccion, CultivosFinca, IngresoFamiliar, OtrosIngresos, TipoCasa, DetalleCasa, Propiedades, Herramientas, Transporte, Ahorro, Credito, Educacion, NoEducacion, Salud, Agua, Seguridad, Recolector, Beneficios, PorqueMiembro, Maderable, Forrajero, Energetico, Frutal, Actividades, Nativos, NoNativos, UsoTierra, Animales, Producto, Cultivos, Rubros, Fuentes, Equipos, Infraestructuras, NombreHerramienta, NombreTransporte,AhorroPregunta, DaCredito, OcupaCredito, Alimentos, Encuesta
from django.contrib.contenttypes import generic
   
class DatosInline(generic.GenericStackedInline):
	model = DatosGenerales
	max_num = 1
	
class OrganizacionInline(generic.GenericStackedInline):
    model = Organizacion
    max_num = 1
    
class MigracionInline(generic.GenericTabularInline):
    model = Migracion
    max_num = 6
    
class TenenciaInline(generic.GenericTabularInline):
    model = Tenencia
    max_num = 1
    
class TierraInline(generic.GenericTabularInline):
    model = Tierra
    max_num = 7
    
class ExistenciaArbolesInline(generic.GenericTabularInline):
    model = ExistenciaArboles
    max_num = 1
    
class ReforestacionInline(generic.GenericTabularInline):
    model = Reforestacion
    extra = 1
    max_num = 9
    
class FincaProduccionInline(generic.GenericTabularInline):
    model = FincaProduccion
    max_num = 12
    
class CultivosFincaInline(generic.GenericTabularInline):
    model = CultivosFinca
    max_num = 11

class IngresoFamiliarInline(generic.GenericTabularInline):
    model = IngresoFamiliar
    max_num = 29

class OtrosIngresosInline(generic.GenericTabularInline):
    model = OtrosIngresos
    max_num = 4
    
class TipoCasaInline(generic.GenericTabularInline):
    model = TipoCasa
    max_num = 1
    
class DetalleCasaInline(generic.GenericTabularInline):
    model = DetalleCasa
    max_num = 1
    
class PropiedadesInline(generic.GenericTabularInline):
    model = Propiedades
    max_num = 8
    
class HerramientasInline(generic.GenericTabularInline):
    model = Herramientas
    max_num = 9
    
class TransporteInline(generic.GenericTabularInline):
    model = Transporte
    max_num = 6
    
class AhorroInline(generic.GenericTabularInline):
    model = Ahorro
    max_num = 6
    
class CreditoInline(generic.GenericTabularInline):
    model = Credito
    max_num = 1
    
class EducacionInline(generic.GenericTabularInline):
    model = Educacion
    max_num = 6
    
class NoEducacionInline(generic.GenericTabularInline):
    model = NoEducacion
    max_num = 4
    
class SaludInline(generic.GenericTabularInline):
    model = Salud
    max_num = 6
    
class AguaInline(generic.GenericTabularInline):
    model = Agua
    extra = 1
    max_num = 6
    
class SeguridadInline(generic.GenericTabularInline):
    model = Seguridad
    max_num = 27
    
class EncuestaAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    inlines = [DatosInline, OrganizacionInline, MigracionInline, TenenciaInline, TierraInline, ExistenciaArbolesInline, ReforestacionInline, FincaProduccionInline, CultivosFincaInline, IngresoFamiliarInline, OtrosIngresosInline, TipoCasaInline, DetalleCasaInline, PropiedadesInline, HerramientasInline, TransporteInline, AhorroInline, CreditoInline, EducacionInline, NoEducacionInline, SaludInline, AguaInline, SeguridadInline]
    
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

