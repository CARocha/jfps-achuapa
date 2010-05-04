from django.contrib import admin
from encuesta.models import Maderable, Forrajero, Energetico, Frutal, ExistenciaArboles, Encuesta
from django.contrib.contenttypes import generic
   
#class ExistenciaArbolesInline(admin.TabularInline):
#    model = ExistenciaArboles
#    
#class ExistenciaArbolesAdmin(admin.ModelAdmin):
#    inlines = [ExistenciaArbolesInline,
#    ]
  
admin.site.register(Maderable)
admin.site.register(Forrajero)
admin.site.register(Energetico)
admin.site.register(Frutal)
admin.site.register(ExistenciaArboles)
