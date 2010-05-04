# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import Municipio
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Esta parte es la de datos generales de las encuestas.

class DatosGenerales(models.Model):
    ''' Datos generales para los encuestados de la jfsp
    '''
    nombre = models.CharField('Nombre de socio o socia', max_length=200)
    cedula = models.CharField('Cedula de socio o socia', max_length=50)
    nombre_finca = models.CharField('Nombre de la Finca', max_length=200)
    comunidad = models.ForeignKey(Municipio)
    coordenada_utm = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Datos Generales"
        
    def __unicode__(self):
        return self.nombre
        
#Fin de datos generales

# Esta parte es la del indicador Organizativo de la JFPS

class Beneficios(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Beneficios Socios"
    def __unicode__(self):
        return self.nombre
        
class PorqueMiembro(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Porque es Miembro"
    def __unicode__(self):
        return self.nombre
            
CHOICE_OPCION = ((1,"Si"),(2,"No"))
CHOICE_DESDE = ((1,"Menos de 5 año"),(2,"Mas de 5 años"))

class Organizacion(models.Model):
    ''' parte de la Organizacion de la cooperativa de achuapa
    '''
    socio = models.IntegerField('Soy socio o socia', choices=CHOICE_OPCION)
    desde_socio = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE)
    socio_cooperativa = models.IntegerField('Mi esposa/esposo es socio(a) de la cooperativa',
                                             choices=CHOICE_OPCION)
    desde_socio_coop = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE)
    hijos_socios = models.IntegerField('Mis Hijos/hijas son socio(as) de la cooperativa', 
                                        choices=CHOICE_OPCION)
    desde_hijo = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE)
    beneficio = models.ForeignKey(Beneficios)
    miembro = models.IntegerField('Soy miembro de la Junta Directiva', 
                                   choices=CHOICE_OPCION)
    desde_miembro = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE)
    no_miembro = models.IntegerField('Si no es miembro de ninguna estructura, estaria interesado en asumir un cargo',
                                      choices=CHOICE_OPCION)
    comision = models.IntegerField('Soy miembro de la comision de trabajo', 
                                    choices=CHOICE_OPCION)
    desde_comision = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE)
    cargo = models.IntegerField('He recibido capasitacion para desempeñar mi cargo', 
                                 choices=CHOICE_OPCION)
    desde_cargo = models.IntegerField('Desde Cuando', choices=CHOICE_DESDE)
    quiero_miembro_junta = models.ForeignKey(PorqueMiembro)
    
    def __unicode__(self):
        return self.str(socio)

# Fin de la parte organizativa

#Indicador Migracion
CHOICE_MIGRACION = ((1,"Hombres adultos (18 años y más)"),(2,"Mujeres adultas (18 años y más)"),(3,"Adolecentes hombres (12 a 17 años)"), (4,"Adolecentes mujeres (12 a 17 años)"),(5,"Niños (menos de 12 años)"),(6,"Niñas (menos de 12 años)"))

class Migracion(models.Model):
    ''' indicador de migracion 
    '''
    edades = models.IntegerField(choices=CHOICE_MIGRACION)
    total_familia = models.IntegerField('Número total en la familia')
    viven_casa = models.IntegerField('Número que viven en la casa o la comunidad')
    viven_fuera = models.IntegerField('Número que viven afuera de la comunidad')
    
    def __unicode__(self):
        return self.str(total_familia)
        
# Fin indicador Migracion

#Indicador tipo de tenencia de parcela y solar
CHOICE_TENENCIA = ((1,"Propia con escritura pública"),(2,"Propia por herencia"),(3,"Propias con promesa de venta"),(4,"Propias con titulo de reforma agraria"),(5,"Arrendada"),(6,"Sin documento"))
CHOICE_DUENO = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),(5,"Colectivo"),(6,"No hay"))

class Tenencia(models.Model):
    ''' que indicador mas raro tipo de tenencia de parcela y solar
    '''
    parcela = models.IntegerField('Parcela (tierra)', choices=CHOICE_TENENCIA)
    solar = models.IntegerField('Solar (dónde está la vivienda)', choices=CHOICE_TENENCIA)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO)
    
    def __unicode__(self):
        return self.str(parcela)

# Fin Tenencia y dueño de propiedad

#Indicador de uso de tierra

class UsoTierra(models.Model):
    nombre = models.CharField(max_length=50)
    
class Tierra(models.Model):
    ''' Aca empieza el indicador de uso de tierra lo deje como llave forania
    porque creo que puede aumentar el uso mas luego '''
    uso_tierra = models.ForeignKey(UsoTierra)
    areas = models.IntegerField('Areas en Mz')
    
    def __unicode__(self):
        return self.uso_tierra.nombre
    
#Fin de indicador uso de tierra

#Indicador existencia de arboles

class Maderable(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    def __unicode__(self):
        return self.nombre
        
class Forrajero(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    def __unicode__(self):
        return self.nombre
        
class Energetico(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    def __unicode__(self):
        return self.nombre
        
class Frutal(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    def __unicode__(self):
        return self.nombre
    
class ExistenciaArboles(models.Model):
    ''' esta clase contiene los tipos de arboles del municipio de 
        achuapa y de la jfps
    '''
    maderable = models.ManyToManyField(Maderable)
    cant_maderable = models.IntegerField()
    forrajero = models.ManyToManyField(Forrajero)
    cant_forrajero = models.IntegerField()
    energetico = models.ManyToManyField(Energetico)
    cant_energetico = models.IntegerField()
    frutal = models.ManyToManyField(Frutal)
    cant_frutal = models.IntegerField()
    
    def __unicode__(self):
        return self.str(cant_maderable)
        
# Fin indicador existencia de arboles

#Indicador reforestacion
class Actividades(models.Model):
    nombre = models.CharField(max_length=100)   
    def __unicode__(self):
        return self.nombre
        
class Nativos(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
class NoNativos(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
class Reforestacion(models.Model):
    '''hay que revisar bien esta tabla esta un poco rara
    '''
    reforestacion = models.ForeignKey(Actividades)
    cantidad_nativos = models.IntegerField()
    cantidad_nonativos = models.IntegerField()
    nativos = models.ManyToMany(Nativos)
    nonativos = models.ManyToMany(NoNativos)
    porciento_nativo = models.IntegerField()
    porciento_nonativo = models.IntegerField()
    
    def __unicode__(self):
        return self.reforestacion.nombre
    
# Fin de indicador de reforestacion

# Indicador animales en la finca y produccion

class Animales(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=20)
    def __unicode__(self):
        return self.nombre
    
class FincaProduccion(models.Model):
    ''' Este indicador lo deje con llave forania para que se ampliable
    '''
    animales = models.ForeignKey(Animales)
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto)
    total_produccion = models.IntegerField('Total producion por año')
    consumo = models.IntegerField('Consumo por año')
    venta = models.IntegerField('Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año')
    
    class Meta:
        verbose_name_plural = "Animales en la finca y produccion"
        
    def __unicode__(self):
        return self.animales.nombre

#Fin indicador animales en la finca y produccion

# Indicador Cultivos en la finca
    
class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
    
class CultivosFinca(models.Model):
    ''' indicador facil XD
    '''
    cultivos = models.ForeignKey(Cultivos)
    total =  models.IntegerField('Total produccion por año')
    consumo = models.IntegerField('Consumo por año')
    venta_libre = models.IntegerField('Venta libre por año')
    venta_organizada = models.IntegerField('Venta organizada por año')
    
    def __unicode__(self):
        return self.cultivos.nombre
    
# Fin del indicador cultivos en la finca

CHOICE_VENDIO = ((1,"Comunidad"),(2,"Intermediario"),(3,"Mercado"),(4,"Cooperativa"))
CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"))
class Rubros(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre
    
class IngresoFamiliar(models.Model):
    ''' otro indicador al parecer facil :p
    '''
    rubro = models.ForeignKey(Rubros)
    cantidad = models.IntegerField('Cantidad vendida por año')
    precio = models.IntegerField('Precio de venta por unidad (Cds)')
    quien_vendio = models.CharField(max_length=50, choices=CHOICE_VENDIO)
    maneja_negocio = models.CharField(max_length=25, choices=CHOICE_MANEJA)
    
    def __unicode__(self):
        return self.rubro.nombre
        
class Fuentes(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.nombre
    
class OtrosIngresos(models.Model):
    ''' algun comentario XD
    '''
    fuente = models.ForeignKey(Fuentes)
    tipo = models.CharField('Tipo de trabajo', max_length=100)
    meses = models.IntegerField('# de meses')
    ingreso = models.IntegerField('Ingreso por mes(Cds)')
    ingreso_total = models.IntegerField('Ingreso total por año(Cds)')
    tiene_ingreso = models.CharField(max_length=25, choices=CHOICE_MANEJA)
    
    def __unicode__(self):
        return self.fuente.nombre
        
#Fin indicador Ingreso familiar

#Indicador de propiedades y bienes
CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))
CHOICE_TIPO_CASA = ((1,"Madera rolliza"),(2,"Adobe"),(3,"Tabla"),(4,"Minifalda"),(5,"Ladrillo o Bloque"))
CHOICE_PISO = ((1,"Tierra"),(2,"Ladrillo de barro"),(3,"Embaldosado"),(4,"Cemento fino"),(5,"ceramica"))
CHOICE_TECHO = ((1,"Plastico"),(2,"Paja"),(3,"Teja de Madera"),(4,"Teja de barro"),(5,"Zinc"))
class TipoCasa(models.Model):
    tipo = models.IntegerField('Tipo de la casa', choices=CHOICE_TIPO_CASA)
    piso = models.IntegerField('Piso de la casa', choices=CHOICE_PISO)
    techo = models.IntegerField('Techo de la casa', choices=CHOICE_TECHO)
    
class DetalleCasa(models.Model):
    tamano = models.IntegerField('Tamaño en mt cuadrado')
    ambientes = models.IntegerField(choices=CHOICE_AMBIENTE)
    letrina = models.IntegerField(choices=CHOICE_OPCION)
    lavadero = models.IntegerField(choices=CHOICE_OPCION)

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre

class Infraestructuras(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre
        
CHOICE_EQUIPO = ((1,"Tiene Luz"),(2,"Con medidor UF"),(3,"Con planta"),(4,"Con panel solar o aeromotor"))        
class Propiedades(models.Model):
    equipo = models.ForeignKey(Equipos)
    cantidad_equipo = models.IntegerField()
    infraestructura = models.ForeignKey(Infraestructuras) 
    cantidad_infra = models.IntegerField('Cantidad')
    tipo_equipo = models.IntegerField(choices=CHOICE_EQUIPO)
    respuesta = models.IntegerField(choices=CHOICE_OPCION)
    
    def __unicode__(self):
        return self.equipo.nombre
    
class Herramientas(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    def __unicode__(self):
        return self.nombre
        
class Transporte(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    def __unicode__(self):
        return self.nombre
    
# Fin indicador de propiedades y bienes

# Indicador de ahorro
CHOICE_AHORRO = ((1,"Si"),(2,"No"),(3,"Menos de 5 años"),(4,"Mas de 5 años"),(5,"Hombre"),(6,"Mujer"),(7,"Ambos"))
class AhorroPregunta(models.Model):
    nombre = models.CharField(max_length=200)   
    def __unicode__(self):
        return self.nombre
    
class Ahorro(models.Model):
    ahorro = models.ForeignKey(AhorroPregunta)
    respuesta = models.IntegerField(choices=CHOICE_AHORRO)
    
    def __unicode__(self):
        return self.ahorro.AhorroPregunta
        
class Credito(models.Model):
    ''' pendiente
    '''
    
# Fin indicador credito

# Indicador Servicio
SEXO_CHOICES=((1,'Hombre mas de 15 años'),(2,'Mujeres mas de 15 años'),(3,'Hombres de 7 a 15 años'),(4,'Mujeres de 7 a 15 años'),(5,'Niños menos de 6 años'),(6,'Niñas menos de 6 años'))
class Educacion(models.Model):
    ''' Indicador muy parecido a fadcanic
    '''
    sexo_edad = models.IntegerField(choices=SEXO_CHOICES)
    num_total = models.IntegerField('Número total')
    no_lee = models.IntegerField('# No sabe leer')
    pri_incompleta = models.IntegerField('# Primaria incompleta')
    pri_completa = models.IntegerField('# Primaria completa')
    secun_incompleta = models.IntegerField('# Secundaria incompleta')
    secun_completa = models.IntegerField('# Secundaria completa')
    estudiante_universitario = models.IntegerField('# Estudiante técnico o universitario')
    tecnico_graduado = models.IntegerField('# Técnica o Universitaria completa') 
    
    def __unicode__(self):
        return self.str(sexo_edad)
        
CHOICE_NINOS_EDUCACION = ((1,'Niños de 3 a 6 años NO asisten a clase'),(2,'Niñas de 3 a 6 años NO asisten a clase'),(3,'Hombres de 7 a 15 años NO asisten a clase'),(4,'Mujeres de 7 a 15 años NO asisten a clase'))

class NoEducacion(models.Model):
    no_asisten = models.IntegerField(choices=CHOICE_NINOS_EDUCACION)
    numero = models.IntegerField()
    razon = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.razon

CHOICE_SALUD = ((1,"Semanal"),(2,"Quinsenal"),(3,"Mensual"),(4,"Semestral"),(5,"Trimestral"),(6,"Anual"))
        
class Salud(models.Model):
    ''' salud de los encuestados aca voy a ocupar el mismo choice de educacion
    '''
    edad = models.IntegerField(choices=SEXO_CHOICES)
    buena_salud = models.IntegerField('# Tiene buena salud')
    delicada_salud = models.IntegerField('# Tiene salud delicada')
    cronica = models.IntegerField('# Tiene enfermedad cronica')
    centro = models.IntegerField('Visita centro de salud', choices=CHOICE_OPCION)
    medico = models.IntegerField('Visita medico privado', choices=CHOICE_OPCION)
    clinica = models.IntegerField('Visita clinica de cooperativa', choices=CHOICE_OPCION)
    nologra = models.IntegerField('# veces en año necesitaban algun servicio de salud y no lograron optenerlo')
    frecuencia = models.IntegerField('Con que frecuencia vista la medico', choices= CHOICE_SALUD)
    
    def __unicode__(self):
        return self.str(edad)

CHOICE_FUENTE_AGUA = ((1,"Quebrada"),(2,"Ojo de agua"),(3,"Pozo comunitario"),(4,"Pozo propio"),(5,"Agua entubada llave comunitaria"),(6,"Agua entubada llave de la casa"))
CHOICE_DISPONIBILIDAD = ((1,"Permanente"),(2,"Temporal(solo invierno)"),(3,"Intermitente(todo el invierno, mitad de verano)"),(4,"TDTH"),(5,"TDAH"),(6,"ADAH"))
CHOICE_CALIDAD_AGUA = ((1,"No potable"),(2,"Potable hirviendo o con filtro"),(3,"Potable"))
          
class Agua(models.Model):
    ''' muy parecido al anterios modelo :P
    '''
    fuente = models.IntegerField(choices= CHOICE_FUENTE_AGUA)
    cantidad = models.IntegerField()
    distancia = models.IntegerField('La distancia de la fuente de la casa en VARAS')
    diponibilidad = models.IntegerField('Disponibilidad de agua en tiempo', choices=CHOICE_DISPONIBILIDAD)
    calidad = models.IntegerField('Calidad del agua', choices= CHOICE_CALIDAD_AGUA)
    
    def __unicode__(self):
        return self.str(fuente)
        
# Fin indicador servicio

#indicador seguridad alimentaria

class Alimentos(models.Model):
    nombre = models.CharField(max_length=80)
    
    def __unicode__(self):
        return self.nombre
        
        
class Seguridad(models.Model):
    ''' Facil modelo
    '''
    alimento = models.ForeignKey(Alimentos)
    producen = models.IntegerField('Producen en la finca',choices=CHOICE_OPCION)
    compran = models.IntegerField('Compran para completar la necesidad',choices=CHOICE_OPCION)
    consumen = models.IntegerField('Consumen lo necesario en los meses de verano', choices=CHOICE_OPCION)
    consumen_invierno = models.IntegerField(Consumen lo necesario en los meses de invierno, choices=CHOICE_OPCION)
    
    def __unicode__(self):
        return self.alimento.nombre    
