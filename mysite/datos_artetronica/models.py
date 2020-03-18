#!/usr/bin/python -tt
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime 

from django.contrib.auth.models import User
#import Image

#from PIL import Image as Img

from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


from django.core.validators import MaxValueValidator


#from sorl.thumbnail import ImageField
from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from django.core.files.base import ContentFile
from django_resized import ResizedImageField

from PIL import Image as Img
#from PIL import Image 

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from io import BytesIO

import sys
from sys import getsizeof


TIPO_USUARIO=(
			('EL_LECTOR', 'EL_LECTOR'),			
			('ENCUESTADOR', 'ENCUESTADOR'),	
			('ADMINISTRADOR', 'ADMINISTRADOR'),
			)
BANCO=(
			('BANCO_AGRICOLA_COMERCIAL', 'BANCO_AGRICOLA_COMERCIAL'),			
			
			)
class UserProfile(models.Model):
		 watsapp=models.CharField(max_length=15)
		 clave=models.CharField(max_length=4)
		 tipo_usuario=models.CharField(max_length=30,blank=True,default="EL_LECTOR",choices=TIPO_USUARIO,null=True)
		 comodin=models.CharField(max_length=12,blank=True,null=True)
		 
		 municipio=models.CharField(max_length=60,blank=True,null=True)
		 departatmento=models.CharField(max_length=60,blank=True,null=True)
		 barrio_colonia_canton_caserio=models.CharField(max_length=160,blank=True,null=True)
		 
		 n_cuenta_ahorro=models.CharField(max_length=60,blank=True,null=True,default="BANCO_AGRICOLA_COMERCIAL",choices=BANCO)
		 banco_a_depositar=models.CharField(max_length=60,blank=True,null=True)
		 nombre_de_la_persona=models.CharField(max_length=60,blank=True,null=True)

		 def __str__(self):
				return  self.watsapp
		 class Admin:
		 	list_display = ('watsapp')

# DESACTIVADO       ACTIVADO


TIPO_ACTIVACION=(
			('DESACTIVADO', 'DESACTIVADO'),			
			('ACTIVO', 'ACTIVO'),	
			
			)
class Codigo(models.Model):
	usuario=models.ForeignKey('UserProfile')
	#codigo=models.CharField(max_length=8,null=True,blank=True)
	estudio=models.ForeignKey('Estudios')

	solicitud_de_activacion=models.CharField(max_length=8,null=True,blank=True,default="DESACTIVADO",choices=TIPO_ACTIVACION)	
	estado_del_estudio=models.CharField(max_length=8,null=True,blank=True,default="DESACTIVADO",choices=TIPO_ACTIVACION)

	cantidad_muestras_asignadas=  models.IntegerField(blank=True,null=True,default=0)
	cantidad_muestras_realizadas=  models.IntegerField(blank=True,null=True,default=0)
	cantidad_muestras_liquidadas= models.IntegerField(blank=True,null=True,default=0)

	fecha_inicio= models.DateField(default=datetime.now)

	comodin=models.CharField(max_length=12,blank=True,null=True)


	def __str__(self):
		return  self.usuario.whatsap
	class Admin:
		list_display = ('codigo')
	    
CATEGORIA_ESTUDIO=(
			('POLITICO', 'POLITICO'),			
			('ECONOMICA', 'ECONOMICA'),
			('PHICOSOCIAL', 'PHICOSOCIAL'),
			('COMERCIAL', 'COMERCIAL'),
			('ACADEMICO', 'ACADEMICO'),
			('CIENTIFICA', 'CIENTIFICA'),
			('DEPORTIVA', 'DEPORTIVA'),
			)



class Categoria(models.Model):
         nombre=models.CharField(max_length=30,blank=True,null=True,default="POLITICO",choices=CATEGORIA_ESTUDIO)
         comodin=models.CharField(max_length=12,blank=True,null=True)
                         
         def __str__(self):
         	return  self.nombre
         class Admin:
         	list_display = ('nombre')



TIPO_ESTUDIO=(
			('PUBLICO', 'PUBLICO'),			
			('DE_PAGO', 'DE_PAGO'),
			('PRIVADO', 'PRIVADO'),							
			)

CONFIANZA_NIVEL=(
			('1.15', '75%'),			
			('1.28', '80%'),
			('1.44', '85%'),	
			('1.65', '90%'),			
			('1.96', '95%'),
			('2.0', '95.5%'),
			('2.58', '99%'),							
			)

class Estudios(models.Model):

		 categoria=models.ForeignKey('Categoria',blank=True,null=True)

		 nombre=models.CharField(max_length=150)
		 descripcion= models.TextField(blank=True,null=True)
		 recomendacion= models.TextField(blank=True,null=True)

		 imagen1 = ImageField(upload_to='tmp',blank=True)
		 fecha_inicio= models.DateField(default=datetime.now)
		 fecha_final= models.DateField(default=datetime.now)
		 fecha_ultima_actualizacion= models.DateField(default=datetime.now)

		 #codigo= models.CharField(max_length=8)
		 tipo_de_estudio= models.CharField(max_length=150,default="PUBLICO",choices=TIPO_ESTUDIO)

		 n_muestras= models.IntegerField(blank=True,null=True)

		
		 universo= models.IntegerField(blank=True,null=True)
		 error= models.CharField(max_length=8,blank=True,null=True)
		 confianza= models.CharField(max_length=8,blank=True,null=True,choices=CONFIANZA_NIVEL,default="1.65")
		 comodin=models.CharField(max_length=12,blank=True,null=True)

		 costo_por_muestra=models.FloatField(default=0,blank=True,null=True)
		 precio_por_suscripcion=models.FloatField(default=5,blank=True,null=True)
		 precio_del_estudio=models.FloatField(default=0,blank=True,null=True)  

		 def save(self, *args,**kwargs):
		 	self.image=self.imagen1
		 	if self.image:
		 	 try:
		 	 	t_image=Img.open(BytesIO(self.image.read()))
		 	 	t_image.thumbnail((360,360),Img.ANTIALIAS)
		 	 	output=BytesIO()
		 	 	t_image.save(output,format='JPEG',quality=75)
		 	 	output.seek(0)
		 	 	self.image=InMemoryUploadedFile(output,'ImageField',"%s.jpg" %self.image.name,'p_image/jpeg',getsizeof(output),None)

		 	 except:
		 	 	pass
		 	super(Estudios,self).save(*args,**kwargs)
		 def __str__(self):
		 	return  self.nombre
		 class Admin:
		 	list_display = ('nombre')



class Preguntas(models.Model):	     
	     estudio=models.ForeignKey('Estudios',blank=True,null=True)
	     pregunta = models.TextField()
     
	     imagen1 = ImageField(upload_to='tmp',blank=True)
	     imagen2 = ImageField(upload_to='tmp',blank=True)
	     imagen3 = ImageField(upload_to='tmp',blank=True)
	     imagen4 = ImageField(upload_to='tmp',blank=True)
	     imagen5 = ImageField(upload_to='tmp',blank=True)
	     imagen6 = ImageField(upload_to='tmp',blank=True)

	     def save(self, *args,**kwargs):
	     	if self.imagen1:
	     		self.image=self.imagen1	     		
	     	elif self.imagen2:
	     		self.image=self.imagen2
	     	elif self.imagen3:
	     		self.image=self.imagen3
	     	elif self.imagen4:
	     		self.image=self.imagen4
	     	elif self.imagen5:
	     		self.image=self.imagen5
	     	elif self.imagen6:
	     		self.image=self.imagen6
	     	else:
	     		self.image=False
	     	
	     	if self.image:
	     	  try:
	     	  	t_image=Img.open(BytesIO(self.image.read()))
	     	  	t_image.thumbnail((360,360),Img.ANTIALIAS)
	     	  	output=BytesIO()
	     	  	t_image.save(output,format='JPEG',quality=75)
	     	  	output.seek(0)
	     	  	self.image=InMemoryUploadedFile(output,'ImageField',"%s.jpg" %self.image.name,'p_image/jpeg',getsizeof(output),None)
	     	  except:
	     	  	pass
	     	super(Preguntas,self).save(*args,**kwargs)


	     def __str__(self):
		    		return  self.pregunta
	     class Admin:
		    		list_display = ('pregunta')
		    		

COLORES=(
			('red', 'ROJO'),	
			('mediumseagrenn', 'TURQUESA'),		
			('blue', 'AZUL'),
			('green', 'VERDE'),
			('cyan', 'ACUA'),
			('orange', 'ANARANJADO'),
			('gray', 'GRIS'),
			('yelow', 'AMARILLO'),			
			('magenta', 'MAGENTA'),
			('pink', 'ROSADO'),
			('darkviolt', 'MORADO'),
			('maroon', 'CAFE'),	
			('lime', 'VERDE LIMA'),		
			('navy', 'AZUL NAVI'),
			('gold', 'MOZTAZA'),
			('lightgray', 'GRIS CLARO'),
			('darkkhaki', 'KAKY'),
			('royalblue', 'AZUL ROYAL'),
			('mmediumpurple', 'MORADO CLARO'),
			('lightsteelblue', 'CELESTE'),
		)


      
class Opciones(models.Model):
		 pregunta=models.ForeignKey('Preguntas',blank=True,null=True)
		 opcion=models.CharField(max_length=100)
		 cantidad= models.IntegerField(blank=True,default=0)
		 color=models.CharField(max_length=30,choices=COLORES)
		 comodin=models.CharField(max_length=12,blank=True,null=True)
		 
		 def __str__(self):
		 	return  self.opcion
		 class Admin:
		 	list_display = ('opcion')

class Opciones_acumuladas(models.Model):
		 pregunta=models.ForeignKey('Preguntas',blank=True,null=True)
		 fecha_de_actualizacion= models.DateField(default=datetime.now)
		 opcion_1=models.IntegerField(blank=True,default=0)
		 opcion_2=models.IntegerField(blank=True,default=0)
		 opcion_3=models.IntegerField(blank=True,default=0)
		 opcion_4=models.IntegerField(blank=True,default=0)
		 opcion_5=models.IntegerField(blank=True,default=0)
		 opcion_6=models.IntegerField(blank=True,default=0)
		 opcion_7=models.IntegerField(blank=True,default=0)
		 opcion_8=models.IntegerField(blank=True,default=0)
		 opcion_9=models.IntegerField(blank=True,default=0)
		 opcion_10=models.IntegerField(blank=True,default=0)
		 opcion_11=models.IntegerField(blank=True,default=0)
		 opcion_12=models.IntegerField(blank=True,default=0)
		 opcion_13=models.IntegerField(blank=True,default=0)
		 opcion_14=models.IntegerField(blank=True,default=0)
		 opcion_15=models.IntegerField(blank=True,default=0)
		 opcion_16=models.IntegerField(blank=True,default=0)
		 opcion_17=models.IntegerField(blank=True,default=0)
		 opcion_18=models.IntegerField(blank=True,default=0)
		 opcion_19=models.IntegerField(blank=True,default=0)
		 opcion_20=models.IntegerField(blank=True,default=0)
		  


		 def __str__(self):
		 	return  self.pregunta.pregunta
		 class Admin:
		 	list_display = ('pregunta')



class Configuracion_sistema(models.Model):
	     mensaje_bienvenida=models.TextField()	
	     n_visitas=models.IntegerField(blank=True,default=0,null=True)
	     comodin=models.CharField(max_length=12,blank=True,null=True) 
	               
	     def __str__(self):
		    		return  self.mensaje_bienvenida
	     class Admin:
		    		list_display = ('mensaje_bienvenida')

	
class Cuestionario_temporal(models.Model):
		 estudio=models.ForeignKey('Estudios',blank=True,null=True)
		 respuesta_1=models.CharField(max_length=100)
		 respuesta_2=models.CharField(max_length=100)
		 respuesta_3=models.CharField(max_length=100)
		 respuesta_4=models.CharField(max_length=100)
		 respuesta_5=models.CharField(max_length=100)
		 respuesta_6=models.CharField(max_length=100)
		 respuesta_7=models.CharField(max_length=100)
		 respuesta_8=models.CharField(max_length=100)
		 respuesta_9=models.CharField(max_length=100)
		 respuesta_10=models.CharField(max_length=100)
		 respuesta_11=models.CharField(max_length=100)
		 respuesta_12=models.CharField(max_length=100)
		 respuesta_13=models.CharField(max_length=100)
		 respuesta_14=models.CharField(max_length=100)
		 respuesta_15=models.CharField(max_length=100)
		 respuesta_16=models.CharField(max_length=100)
		 respuesta_17=models.CharField(max_length=100)
		 respuesta_18=models.CharField(max_length=100)
		 respuesta_19=models.CharField(max_length=100)
		 respuesta_20=models.CharField(max_length=100)
		 respuesta_21=models.CharField(max_length=100)
		 respuesta_22=models.CharField(max_length=100)
		 respuesta_23=models.CharField(max_length=100)
		 respuesta_24=models.CharField(max_length=100)
		 respuesta_25=models.CharField(max_length=100)
		 respuesta_26=models.CharField(max_length=100)
		 respuesta_27=models.CharField(max_length=100)
		 respuesta_28=models.CharField(max_length=100)
		 respuesta_29=models.CharField(max_length=100)
		 respuesta_30=models.CharField(max_length=100)
		 respuesta_31=models.CharField(max_length=100)
		 respuesta_32=models.CharField(max_length=100)
		 respuesta_33=models.CharField(max_length=100)
		 respuesta_34=models.CharField(max_length=100)
		 respuesta_35=models.CharField(max_length=100)
		 respuesta_36=models.CharField(max_length=100)
		 respuesta_37=models.CharField(max_length=100)
		 respuesta_38=models.CharField(max_length=100)
		 respuesta_39=models.CharField(max_length=100)
		 respuesta_40=models.CharField(max_length=100)
		 respuesta_41=models.CharField(max_length=100)
		 respuesta_42=models.CharField(max_length=100)
		 respuesta_43=models.CharField(max_length=100)
		 respuesta_44=models.CharField(max_length=100)
		 respuesta_45=models.CharField(max_length=100)
		 respuesta_46=models.CharField(max_length=100)
		 respuesta_47=models.CharField(max_length=100)
		 respuesta_48=models.CharField(max_length=100)
		 respuesta_49=models.CharField(max_length=100)
		 respuesta_50=models.CharField(max_length=100)

		 encuestador=models.CharField(max_length=15)
		 fecha_de_ingreso = models.DateField(default=datetime.now)
		 
		 comodin=models.CharField(max_length=12,blank=True,null=True)
		 
		 def __str__(self):
		 	return  self.estudio.nombre
		 class Admin:
		 	list_display = ('estudio.nombre')

class Cuestionario_principal(models.Model):
		 estudio=models.ForeignKey('Estudios',blank=True,null=True)
		 respuesta_1=models.CharField(max_length=100)
		 respuesta_2=models.CharField(max_length=100)
		 respuesta_3=models.CharField(max_length=100)
		 respuesta_4=models.CharField(max_length=100)
		 respuesta_5=models.CharField(max_length=100)
		 respuesta_6=models.CharField(max_length=100)
		 respuesta_7=models.CharField(max_length=100)
		 respuesta_8=models.CharField(max_length=100)
		 respuesta_9=models.CharField(max_length=100)
		 respuesta_10=models.CharField(max_length=100)
		 respuesta_11=models.CharField(max_length=100)
		 respuesta_12=models.CharField(max_length=100)
		 respuesta_13=models.CharField(max_length=100)
		 respuesta_14=models.CharField(max_length=100)
		 respuesta_15=models.CharField(max_length=100)
		 respuesta_16=models.CharField(max_length=100)
		 respuesta_17=models.CharField(max_length=100)
		 respuesta_18=models.CharField(max_length=100)
		 respuesta_19=models.CharField(max_length=100)
		 respuesta_20=models.CharField(max_length=100)
		 respuesta_21=models.CharField(max_length=100)
		 respuesta_22=models.CharField(max_length=100)
		 respuesta_23=models.CharField(max_length=100)
		 respuesta_24=models.CharField(max_length=100)
		 respuesta_25=models.CharField(max_length=100)
		 respuesta_26=models.CharField(max_length=100)
		 respuesta_27=models.CharField(max_length=100)
		 respuesta_28=models.CharField(max_length=100)
		 respuesta_29=models.CharField(max_length=100)
		 respuesta_30=models.CharField(max_length=100)
		 respuesta_31=models.CharField(max_length=100)
		 respuesta_32=models.CharField(max_length=100)
		 respuesta_33=models.CharField(max_length=100)
		 respuesta_34=models.CharField(max_length=100)
		 respuesta_35=models.CharField(max_length=100)
		 respuesta_36=models.CharField(max_length=100)
		 respuesta_37=models.CharField(max_length=100)
		 respuesta_38=models.CharField(max_length=100)
		 respuesta_39=models.CharField(max_length=100)
		 respuesta_40=models.CharField(max_length=100)
		 respuesta_41=models.CharField(max_length=100)
		 respuesta_42=models.CharField(max_length=100)
		 respuesta_43=models.CharField(max_length=100)
		 respuesta_44=models.CharField(max_length=100)
		 respuesta_45=models.CharField(max_length=100)
		 respuesta_46=models.CharField(max_length=100)
		 respuesta_47=models.CharField(max_length=100)
		 respuesta_48=models.CharField(max_length=100)
		 respuesta_49=models.CharField(max_length=100)
		 respuesta_50=models.CharField(max_length=100)

		 encuestador=models.CharField(max_length=15)
		 fecha_de_ingreso = models.DateField(default=datetime.now)
		 
		 comodin=models.CharField(max_length=12,blank=True,null=True)
		 
		 def __str__(self):
		 	return  self.estudio.nombre
		 class Admin:
		 	list_display = ('estudio.nombre')
