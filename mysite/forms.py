#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django import forms


class UserProfileForm(ModelForm):
	class Meta:
		model= UserProfile
		exclude=['tipo_usuario']

class CodigoForm(ModelForm):
	class Meta:
		model= Codigo	
		exclude=[]


class EstudiosForm(ModelForm):
	class Meta:
		model= Estudios
		widgets = {'descripcion': Textarea(attrs={'cols': 30, 'rows': 2}),'descripcion_publica': Textarea(attrs={'cols': 30, 'rows': 2}),}
		exclude=["codigo","n_muestras","universo","patrocinador_1","patrocinador_2","fecha_final_plan","nota_de_evaluacion"]
		

class PreguntasForm(ModelForm):
	class Meta:
		model= Preguntas
		exclude=[]
		widgets = {'pregunta': Textarea(attrs={'cols': 30, 'rows': 2}),}
		

class OpcionesForm(ModelForm):
	class Meta:
		model= Opciones		
		exclude=[]
	
	def __init__(self, nombre_pregunta,*args, **kwargs):
		super(OpcionesForm, self).__init__(*args, **kwargs)		
		self.fields['pregunta'].queryset=Preguntas.objects.filter(pregunta=nombre_pregunta)

class Cuestionario_principalForm(ModelForm):
	class Meta:
		model= Cuestionario_principal	
		exclude=[]
	
	

class Configuracion_sistemaForm(ModelForm):
	class Meta:
			
		model=Configuracion_sistema
		widgets = {'mensaje_bienvenida': Textarea(attrs={'cols': 30, 'rows': 2}),'respuesta': Textarea(attrs={'cols': 30, 'rows': 3}),}
		exclude=[]