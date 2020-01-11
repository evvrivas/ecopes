#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mysite.datos_artetronica.models import *

from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django import forms


class UserProfileForm(ModelForm):
	class Meta:
		model= Usuarios	
		exclude=[]

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
		self.fields['pregunta'].queryset=Preguntas.objects.filter(nombre=nombre_pregunta)


class RespuestasForm(ModelForm):
	class Meta:
		model= Respuestas
		
	def __init__(self, nombre_opcion,*args, **kwargs):
		super(RespuestasForm, self).__init__(*args, **kwargs)		
		self.fields['opcion'].queryset=Opciones.objects.filter(tienda=nombre_opcion)

