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
			)

PLAN= (
	        ('GRATIS', 'GRATIS (Solo puedes ver limitadamente)  '), 
			('MUNICIPAL', 'MUNICIPAL (Solo puedes ver los estudios de un Municipio)'),
			('DEPARTAMENTAL', 'DEPARTAMENTAL (Solo puedes ver los estudios del departamento)'),
			('NACIONAL', 'NACIONAL (Ver todos los estudios del pais))'),						       
			)

                                                                                           
ESTADO_USUARIO=(
			('DE_ALTA', 'DE_ALTA'),			
			('DE_BAJA', 'DE_BAJA'),							
			)				


class UserProfile(models.Model):
		 usuario=models.CharField(max_length=30)
		 tipo_usuario=models.CharField(max_length=30,choices=TIPO_USUARIO,blank=True,default="EL_LECTOR",null=True)
		 codigo=models.CharField(max_length=30,blank=True,null=True)
		 def __unicode__(self):
		 	return u'Profile of user: %s' % self.usuario.username
		 class Admin:
		 	list_display = ('tipo_usuario')



class Codigo(models.Model):
	usuario=models.CharField(max_length=30)
	codigo=models.CharField(max_length=30,null=True,blank=True)
	def __str__(self):
		return  self.codigo
	class Admin:
		list_display = ('codigo')
	    


class Estudios(models.Model):

		 nombre=models.CharField(max_length=150)
		 descripcion= models.TextField(blank=True)
		 descripcion_publica= models.TextField(blank=True)
		 imagen1 = ImageField(upload_to='tmp',blank=True)

		 fecha_inicio= models.DateField(default=datetime.now)
		 fecha_final= models.DateField(default=datetime.now)
		 codigo= models.CharField(max_length=150)

		 n_muestras= models.IntegerField(blank=True)
		 universo= models.IntegerField(blank=True)

		 patrocinador_1= models.CharField(max_length=150)
		 patrocinador_2= models.CharField(max_length=150)

		 def save(self, *args,**kwargs):
		 	self.image=self.imagen1
		 	if self.image:
		 		t_image=Img.open(BytesIO(self.image.read()))
		 		t_image.thumbnail((360,360),Img.ANTIALIAS)
		 		output=BytesIO()
		 		t_image.save(output,format='JPEG',quality=75)
		 		output.seek(0)
		 		self.image=InMemoryUploadedFile(output,'ImageField',"%s.jpg" %self.image.name,'p_image/jpeg',getsizeof(output),None)
		 	super(Tiendas,self).save(*args,**kwargs)
		 def __str__(self):
		 	return  self.nombre
		 class Admin:
		 	list_display = ('nombre')



class Preguntas(models.Model):	     
	     estudio=models.ForeignKey('Estudios',blank=True,null=True)
	     pregunta = models.TextField(blank=True)
     
	     imagen1 = ImageField(upload_to='tmp',blank=True)
	     imagen2 = ImageField(upload_to='tmp',blank=True)
	     imagen3 = ImageField(upload_to='tmp',blank=True)


	     def save(self, *args,**kwargs):
	     	if self.imagen1:
	     		self.image=self.imagen1
	     		
	     	elif self.imagen2:
	     		self.image=self.imagen2
	     	elif self.imagen3:
	     		self.image=self.imagen3
	     	else:
	     		pass
	     	
	     	if self.image:
	     		t_image=Img.open(BytesIO(self.image.read()))
	     		t_image.thumbnail((360,360),Img.ANTIALIAS)
	     		output=BytesIO()
	     		t_image.save(output,format='JPEG',quality=75)
	     		output.seek(0)
	     		self.image=InMemoryUploadedFile(output,'ImageField',"%s.jpg" %self.image.name,'p_image/jpeg',getsizeof(output),None)
	     	super(Productos,self).save(*args,**kwargs)


	     def __str__(self):
		    		return  self.nombre
	     class Admin:
		    		list_display = ('categoria', 'cantidad', 'nombre','precio_A')
		    		

class Opciones(models.Model):
		 pregunta=models.ForeignKey('Preguntas',blank=True,null=True)
		 opcion=models.CharField(max_length=60,blank=True)
		 def __str__(self):
		 	return  self.opcion
		 class Admin:
		 	list_display = ('opcion')


class Respuestas(models.Model):
	opcion=models.ForeignKey('Opciones',blank=True,null=True)
	respuesta=models.CharField(max_length=60,blank=True)
	def __str__(self):
		return  self.respuesta
	class Admin:
		list_display = ('respuesta')




