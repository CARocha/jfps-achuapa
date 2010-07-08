# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import Comunidad
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Esta parte es la de datos generales de las encuestas.

CHOICE_SEX = ((1,'Hombre'),(2,'Mujer'))

class Cooperativa(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class DatosGenerales(models.Model):
    ''' Datos generales para los encuestados de la jfsp
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    nombre = models.CharField('Nombre de socio o socia', max_length=200)
    sexo = models.IntegerField('Sexo del Socio/a',choices=CHOICE_SEX, null=True, blank=True)
    coop = models.ForeignKey('Cooperativa a la que pertenece el socio/a', Cooperativa, null=True, blank=True)
    cedula = models.CharField('Cedula de socio o socia', max_length=50)
    nombre_finca = models.CharField('Nombre de la Finca', max_length=200)
    comunidad = models.ForeignKey(Comunidad)
    coordenada_lt = models.DecimalField(max_digits=24, decimal_places=16, blank=True, null=True)
    coordenada_lg = models.DecimalField(max_digits=24, decimal_places=16, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Datos Generales"
        
    def __unicode__(self):
        return self.nombre
        
#Fin de datos generales

# Esta parte es la del indicador Organizativo de la JFPS

class Beneficios(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Organizacion-Beneficios Socios"
    def __unicode__(self):
        return self.nombre
        
class PorqueMiembro(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Organizacion-Porque es Miembro"
    def __unicode__(self):
        return self.nombre
            
CHOICE_OPCION = ((1,"Si"),(2,"No"))
CHOICE_DESDE = ((1,"Menos de 5 año"),(2,"Mas de 5 años"))

class Organizacion(models.Model):
    ''' parte de la Organizacion de la cooperativa de achuapa
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    socio = models.IntegerField('Soy socio o socia', choices=CHOICE_OPCION)
    desde_socio = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE,blank=True, null=True)
    socio_cooperativa = models.IntegerField('Mi esposa/esposo es socio(a) de la cooperativa',
                                             choices=CHOICE_OPCION)
    desde_socio_coop = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE, blank=True, null=True)
    hijos_socios = models.IntegerField('Mis Hijos/hijas son socio(as) de la cooperativa', 
                                        choices=CHOICE_OPCION)
    desde_hijo = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE, blank=True, null=True)
    beneficio = models.ManyToManyField(Beneficios, verbose_name="Beneficios obtenidos", blank=True, null=True)
    miembro = models.IntegerField('Soy miembro de la Junta Directiva', 
                                   choices=CHOICE_OPCION)
    desde_miembro = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE, blank=True, null=True)
    no_miembro = models.IntegerField('Si no es miembro de ninguna estructura, estaria interesado en asumir un cargo',
                                      choices=CHOICE_OPCION)
    comision = models.IntegerField('Soy miembro de la comision de trabajo', 
                                    choices=CHOICE_OPCION)
    desde_comision = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE, blank=True, null=True)
    cargo = models.IntegerField('He recibido capacitación para desempeñar mi cargo', 
                                 choices=CHOICE_OPCION)
    desde_cargo = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE,blank=True, null=True)
    quiero_miembro_junta = models.ManyToManyField(PorqueMiembro, verbose_name="Quiero ser miembro de junta", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Organizacion"   
    def __unicode__(self):
        return str('%s' % (self.socio))

# Fin de la parte organizativa

#Indicador Migracion
CHOICE_MIGRACION = ((1,"Hombres adultos (18 años y más)"),(2,"Mujeres adultas (18 años y más)"),(3,"Adolecentes hombres (12 a 17 años)"), (4,"Adolecentes mujeres (12 a 17 años)"),(5,"Niños (menos de 12 años)"),(6,"Niñas (menos de 12 años)"))

class Migracion(models.Model):
    ''' indicador de migracion 
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    edades = models.IntegerField(choices=CHOICE_MIGRACION)
    total_familia = models.IntegerField('Número total en la familia')
    viven_casa = models.IntegerField('Número que viven en la casa o la comunidad')
    viven_fuera = models.IntegerField('Número que viven afuera de la comunidad')
    
    class Meta:
        verbose_name_plural = "Migración"
#    def __unicode__(self):
#        return self.str(total_familia)
        
# Fin indicador Migracion

#Indicador tipo de tenencia de parcela y solar
CHOICE_TENENCIA = ((1,"Propia con escritura pública"),(2,"Propia por herencia"),(3,"Propias con promesa de venta"),(4,"Propias con titulo de reforma agraria"),(5,"Arrendada"),(6,"Sin documento"))
CHOICE_DUENO = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),(5,"Colectivo"),(6,"No hay"))

class Tenencia(models.Model):
    ''' que indicador mas raro tipo de tenencia de parcela y solar
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    parcela = models.IntegerField('Parcela (tierra)', choices=CHOICE_TENENCIA)
    solar = models.IntegerField('Solar (dónde está la vivienda)', choices=CHOICE_TENENCIA)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO)
    
    class Meta:
        verbose_name_plural = "Tenencia"
#    def __unicode__(self):
#        return self.str(parcela)

# Fin Tenencia y dueño de propiedad

#Indicador de uso de tierra

class UsoTierra(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name_plural = "Tierra-Tipo de uso de Tierra"
    def __unicode__(self):
        return self.nombre
    
class Tierra(models.Model):
    ''' Aca empieza el indicador de uso de tierra lo deje como llave forania
    porque creo que puede aumentar el uso mas luego '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    uso_tierra = models.ForeignKey(UsoTierra)
    areas = models.IntegerField('Areas en Mz')
    
    class Meta:
        verbose_name_plural = "Uso de Tierra"
    def __unicode__(self):
        return self.uso_tierra.nombre
    
#Fin de indicador uso de tierra

#Indicador existencia de arboles

class Maderable(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Existencia de Arboles-Maderable"
    def __unicode__(self):
        return self.nombre
        
class Forrajero(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Existencia de Arboles-Forrajero"
    def __unicode__(self):
        return self.nombre
        
class Energetico(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Existencia de Arboles-Energetico"
    def __unicode__(self):
        return self.nombre
        
class Frutal(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Existencia de Arboles-Frutal"
    def __unicode__(self):
        return self.nombre
    
class ExistenciaArboles(models.Model):
    ''' esta clase contiene los tipos de arboles del municipio de 
        achuapa y de la jfps
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    maderable = models.ManyToManyField(Maderable, blank=True, null=True)
    cant_maderable = models.IntegerField()
    forrajero = models.ManyToManyField(Forrajero, blank=True, null=True)
    cant_forrajero = models.IntegerField()
    energetico = models.ManyToManyField(Energetico, blank=True, null=True)
    cant_energetico = models.IntegerField()
    frutal = models.ManyToManyField(Frutal, blank=True, null=True)
    cant_frutal = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Existencia de Arboles"
#    def __unicode__(self):
#        return self.str(cant_maderable)
        
# Fin indicador existencia de arboles

#Indicador reforestacion
class Actividades(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Reforestación-Actividades"   
    def __unicode__(self):
        return self.nombre
        
class Nativos(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Reforestación-Nativos"
    def __unicode__(self):
        return self.nombre
        
class NoNativos(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Reforestación-NoNativos"
    def __unicode__(self):
        return self.nombre
        
class Reforestacion(models.Model):
    '''hay que revisar bien esta tabla esta un poco rara
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    reforestacion = models.ForeignKey(Actividades)
    cantidad_nativos = models.IntegerField()
    cantidad_nonativos = models.IntegerField()
    nativos = models.ManyToManyField(Nativos, blank=True, null=True)
    nonativos = models.ManyToManyField(NoNativos, blank=True, null=True)
    porciento_nativo = models.IntegerField()
    porciento_nonativo = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Reforestación"
    def __unicode__(self):
        return self.reforestacion.nombre
    
# Fin de indicador de reforestacion

# Indicador animales en la finca y produccion

class Animales(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "FincaProduccion-Animales"
    def __unicode__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "FincaProduccion-Producto"
    def __unicode__(self):
        return self.nombre
    
class FincaProduccion(models.Model):
    ''' Este indicador lo deje con llave forania para que se ampliable
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    animales = models.ForeignKey(Animales)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto)
    total_produccion = models.IntegerField('Total producion por año')
    consumo = models.IntegerField('Consumo por año')
    venta = models.IntegerField('Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año')
    
    class Meta:
        verbose_name_plural = "Finca y produccion"        
    def __unicode__(self):
        return self.animales.nombre

#Fin indicador animales en la finca y produccion

# Indicador Cultivos en la finca
    
class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "CultivosFinca-Cultivos"
    def __unicode__(self):
        return self.nombre
    
class CultivosFinca(models.Model):
    ''' indicador facil XD
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    cultivos = models.ForeignKey(Cultivos)
    total =  models.IntegerField('Total produccion por año')
    consumo = models.IntegerField('Consumo por año')
    venta_libre = models.IntegerField('Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año')
    
    class Meta:
        verbose_name_plural = "Cultivos de la Finca"
    def __unicode__(self):
        return self.cultivos.nombre
    
# Fin del indicador cultivos en la finca

CHOICE_VENDIO = ((1,"Comunidad"),(2,"Intermediario"),(3,"Mercado"),(4,"Cooperativa"))
CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"))
class Rubros(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "IngresoFamiliar-Rubros"
    def __unicode__(self):
        return self.nombre
    
class IngresoFamiliar(models.Model):
    ''' otro indicador al parecer facil :p
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    rubro = models.ForeignKey(Rubros)
    cantidad = models.IntegerField('Cantidad vendida por año')
    precio = models.IntegerField('Precio de venta por unidad (Cds)')
    quien_vendio = models.IntegerField(choices=CHOICE_VENDIO)
    maneja_negocio = models.IntegerField(choices=CHOICE_MANEJA)
    
    class Meta:
        verbose_name_plural = "Ingreso Familiar"
    def __unicode__(self):
        return self.rubro.nombre
        
class Fuentes(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "OtrosIngresoFamiliar-Fuentes"
    def __unicode__(self):
        return self.nombre
    
class OtrosIngresos(models.Model):
    ''' algun comentario XD
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    fuente = models.ForeignKey(Fuentes)
    tipo = models.CharField('Tipo de trabajo', max_length=100)
    meses = models.IntegerField('# de meses')
    ingreso = models.IntegerField('Ingreso por mes(Cds)')
    ingreso_total = models.IntegerField('Ingreso total por año(Cds)')
    tiene_ingreso = models.IntegerField(choices=CHOICE_MANEJA)
    
    class Meta:
        verbose_name_plural = "Otros Ingresos"
    def __unicode__(self):
        return self.fuente.nombre
        
#Fin indicador Ingreso familiar

#Indicador de propiedades y bienes
CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))
CHOICE_TIPO_CASA = ((1,"Madera rolliza"),(2,"Adobe"),(3,"Tabla"),(4,"Minifalda"),(5,"Ladrillo o Bloque"))
class Piso(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
class Techo(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
#CHOICE_PISO = ((1,"Tierra"),(2,"Ladrillo de barro"),(3,"Embaldosado"),(4,"Cemento fino"),(5,"ceramica"))
#CHOICE_TECHO = ((1,"Plastico"),(2,"Paja"),(3,"Teja de Madera"),(4,"Teja de barro"),(5,"Zinc"))
class TipoCasa(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    tipo = models.IntegerField('Tipo de la casa', choices=CHOICE_TIPO_CASA)
    piso = models.ManyToManyField(Piso, verbose_name="Piso")
    techo = models.ManyToManyField(Techo, verbose_name="Techo")
    
    class Meta:
        verbose_name_plural = "Tipos de Casas"
    
class DetalleCasa(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    tamano = models.IntegerField('Tamaño en mt cuadrado')
    ambientes = models.IntegerField(choices=CHOICE_AMBIENTE)
    letrina = models.IntegerField(choices=CHOICE_OPCION)
    lavadero = models.IntegerField(choices=CHOICE_OPCION)
    
    class Meta:
        verbose_name_plural = "Detalles de la Casa"

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Propiedades-Equipos"    
    def __unicode__(self):
        return self.nombre

class Infraestructuras(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Propiedades-Infraestructura"
    def __unicode__(self):
        return self.nombre
        
CHOICE_EQUIPO = ((1,"Tiene Luz"),(2,"Con medidor UF"),(3,"Con planta"),(4,"Con panel solar o aeromotor"))        
class Propiedades(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    equipo = models.ForeignKey(Equipos, blank=True, null=True)
    cantidad_equipo = models.IntegerField(blank=True, null=True)
    infraestructura = models.ForeignKey(Infraestructuras, blank=True, null=True) 
    cantidad_infra = models.IntegerField('Cantidad', blank=True, null=True)
    tipo_equipo = models.IntegerField(choices=CHOICE_EQUIPO, null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Equipos"
#    def __unicode__(self):
#        return self.equipo.nombre
        
class NombreHerramienta(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Herramientas-Nombres"
    def __unicode__(self):
        return self.nombre
    
class Herramientas(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    herramienta = models.ForeignKey(NombreHerramienta)
    numero = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Herramientas"
    def __unicode__(self):
        return self.herramienta.nombre
        
class NombreTransporte(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Transporte-Nombre"
    def __unicode__(self):
        return self.nombre
        
class Transporte(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    transporte = models.ForeignKey(NombreTransporte)
    numero = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Transporte"
    
# Fin indicador de propiedades y bienes

# Indicador de ahorro
CHOICE_AHORRO = ((1,"Si"),(2,"No"),(3,"Menos de 5 años"),(4,"Mas de 5 años"),(5,"Hombre"),(6,"Mujer"),(7,"Ambos"))
class AhorroPregunta(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Ahorro-Preguntas"   
    def __unicode__(self):
        return self.nombre
    
class Ahorro(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    ahorro = models.ForeignKey(AhorroPregunta)
    respuesta = models.IntegerField(choices=CHOICE_AHORRO)
    
    class Meta:
        verbose_name_plural = "Ahorro"
    def __unicode__(self):
        return self.ahorro.nombre

class DaCredito(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Credito-Dacredito"
    def __unicode__(self):
        return self.nombre
        
class OcupaCredito(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Credito-Ocupa"
    def __unicode__(self):
        return self.nombre
CHOICE_SATISFACCION = ((1,"Menos de 25 % de las necesidades"),(2,"Entre 25 y 50 % de las necesidades"),(3,"Entre 50 y 100 % de las necesidades"))
        
class Credito(models.Model):
    ''' El credito de los miembros de jfps
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    recibe = models.IntegerField('Recibe Crédito', choices= CHOICE_OPCION)
    desde = models.IntegerField('Desde cuando', choices= CHOICE_DESDE, blank=True, null=True)
    quien_credito = models.ManyToManyField(DaCredito, verbose_name="De quien recibe credito")
    ocupa_credito = models.ManyToManyField(OcupaCredito, verbose_name="Para que ocupa el credito")
    satisfaccion = models.IntegerField('Satisfacción de la demanda de crédito', choices= CHOICE_SATISFACCION, blank=True, null=True)
    dia = models.IntegerField('Esta al dia con su Crédito', choices=CHOICE_OPCION, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Crédito"
#    def __unicode__(self):
#        return self.str(recibe)    
#    
# Fin indicador credito

# Indicador Servicio
SEXO_CHOICES=((1,'Hombre mas de 15 años'),(2,'Mujeres mas de 15 años'),(3,'Hombres de 7 a 15 años'),(4,'Mujeres de 7 a 15 años'),(5,'Niños menos de 6 años'),(6,'Niñas menos de 6 años'))
class Educacion(models.Model):
    ''' Indicador muy parecido a fadcanic
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    sexo_edad = models.IntegerField(choices=SEXO_CHOICES)
    num_total = models.IntegerField('Número total')
    no_lee = models.IntegerField('# No sabe leer')
    pri_incompleta = models.IntegerField('# Primaria incompleta')
    pri_completa = models.IntegerField('# Primaria completa')
    secun_incompleta = models.IntegerField('# Secundaria incompleta')
    secun_completa = models.IntegerField('# Secundaria completa')
    estudiante_universitario = models.IntegerField('# Estudiante técnico o universitario')
    tecnico_graduado = models.IntegerField('# Técnica o Universitaria completa') 
    
    class Meta:
        verbose_name_plural = "Servicio - Educación"
#    def __unicode__(self):
#        return self.str(sexo_edad)
        
CHOICE_NINOS_EDUCACION = ((1,'Niños de 3 a 6 años NO asisten a clase'),(2,'Niñas de 3 a 6 años NO asisten a clase'),(3,'Hombres de 7 a 15 años NO asisten a clase'),(4,'Mujeres de 7 a 15 años NO asisten a clase'))

class NoEducacion(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    no_asisten = models.IntegerField(choices=CHOICE_NINOS_EDUCACION)
    numero = models.IntegerField()
    razon = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Porque No Estudia"
    def __unicode__(self):
        return self.razon

CHOICE_SALUD = ((1,"Semanal"),(2,"Quinsenal"),(3,"Mensual"),(4,"Semestral"),(5,"Trimestral"),(6,"Anual"))
        
class Salud(models.Model):
    ''' salud de los encuestados aca voy a ocupar el mismo choice de educacion
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    edad = models.IntegerField(choices=SEXO_CHOICES)
    buena_salud = models.IntegerField('# Tiene buena salud')
    delicada_salud = models.IntegerField('# Tiene salud delicada')
    cronica = models.IntegerField('# Tiene enfermedad cronica')
    centro = models.IntegerField('Visita centro de salud', choices=CHOICE_OPCION, blank=True, null=True)
    medico = models.IntegerField('Visita medico privado', choices=CHOICE_OPCION, blank=True, null=True)
    clinica = models.IntegerField('Visita clinica de cooperativa', choices=CHOICE_OPCION, blank=True, null=True)
    nologra = models.IntegerField('# veces en año necesitaban algun servicio de salud y no lograron optenerlo')
    frecuencia = models.IntegerField('Con que frecuencia vista la medico', choices= CHOICE_SALUD, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Salud"
#    def __unicode__(self):
#        return self.str(edad)

CHOICE_FUENTE_AGUA = ((1,"Quebrada"),(2,"Ojo de agua"),(3,"Pozo comunitario"),(4,"Pozo propio"),(5,"Agua entubada llave comunitaria"),(6,"Agua entubada llave de la casa"))
CHOICE_DISPONIBILIDAD = ((1,"Permanente"),(2,"Temporal(solo invierno)"),(3,"Intermitente(todo el invierno, mitad de verano)"),(4,"TDTH"),(5,"TDAH"),(6,"ADAH"))
CHOICE_CALIDAD_AGUA = ((1,"No potable"),(2,"Potable hirviendo o con filtro"),(3,"Potable"))
          
class Agua(models.Model):
    ''' muy parecido al anterios modelo :P
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    fuente = models.IntegerField(choices= CHOICE_FUENTE_AGUA)
    cantidad = models.IntegerField()
    distancia = models.IntegerField('La distancia de la fuente de la casa en VARAS')
    diponibilidad = models.IntegerField('Disponibilidad de agua en tiempo', choices=CHOICE_DISPONIBILIDAD)
    calidad = models.IntegerField('Calidad del agua', choices= CHOICE_CALIDAD_AGUA)
    
    class Meta:
        verbose_name_plural = "Agua"
#    def __unicode__(self):
#        return self.str(fuente)
        
# Fin indicador servicio

#indicador seguridad alimentaria

class Alimentos(models.Model):
    nombre = models.CharField(max_length=80)
    class Meta:
        verbose_name_plural = "Seguridad-Alimento"
    def __unicode__(self):
        return self.nombre
        
        
class Seguridad(models.Model):
    ''' Fácil modelo
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey()
    alimento = models.ForeignKey(Alimentos)
    producen = models.IntegerField('Producen en la finca',choices=CHOICE_OPCION)
    compran = models.IntegerField('Compran para completar la necesidad',choices=CHOICE_OPCION)
    consumen = models.IntegerField('Consumen lo necesario en los meses de verano', choices=CHOICE_OPCION)
    consumen_invierno = models.IntegerField('Consumen lo necesario en los meses de invierno', choices=CHOICE_OPCION)
    
    class Meta:
        verbose_name_plural = "Seguridad alimentaria"
    def __unicode__(self):
        return self.alimento.nombre

# Fin del indicador seguridad alimentaria

# Inicio de la tabla que controla todos los indicadores

class Recolector(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Recolector"
    def __unicode__(self):
        return self.nombre

class Encuesta(models.Model):
    fecha = models.DateField()
    recolector = models.ForeignKey(Recolector)
    datos = generic.GenericRelation(DatosGenerales)
    organizacion = generic.GenericRelation(Organizacion)
    migracion = generic.GenericRelation(Migracion)
    tenencia = generic.GenericRelation(Tenencia)
    tierra = generic.GenericRelation(Tierra)
    existenciarboles = generic.GenericRelation(ExistenciaArboles)
    reforestacion = generic.GenericRelation(Reforestacion)
    fincaproduccion = generic.GenericRelation(FincaProduccion)
    cultivosfinca = generic.GenericRelation(CultivosFinca)
    ingresofamialiar = generic.GenericRelation(IngresoFamiliar)
    otrosingreso = generic.GenericRelation(OtrosIngresos)
    tipocasa = generic.GenericRelation(TipoCasa)
    detallecasa = generic.GenericRelation(DetalleCasa)
    propiedades = generic.GenericRelation(Propiedades)
    herramientas = generic.GenericRelation(Herramientas)
    transporte = generic.GenericRelation(Transporte)
    ahorro = generic.GenericRelation(Ahorro)
    credito = generic.GenericRelation(Credito)
    educacion = generic.GenericRelation(Educacion)
    noeducacion = generic.GenericRelation(NoEducacion)
    salud = generic.GenericRelation(Salud)
    agua = generic.GenericRelation(Agua)
    seguridad = generic.GenericRelation(Seguridad)
    
    def __unicode__(self):
        return self.datos.all()[0].nombre
        
    def nombre_datos(self):
        return self.datos.all()[0].datos
    def nombre_socios(self):
        return self.datos.all()[0].nombre
    def comunidades(self):
        return self.datos.all()[0].comunidad
    def municipios(self):
        return self.datos.all()[0].comunidad.municipio
