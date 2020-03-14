
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from mysite.datos_artetronica.models import *


#admin.site.unregister(User)
from mysite.forms import *

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = UserProfileForm
class UserProfileAdmin(admin.ModelAdmin):
        model = UserProfile
        list_display = ['watsapp','tipo_usuario']
          
admin.site.register(UserProfile,UserProfileAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = CodigoForm
class CodigoAdmin(admin.ModelAdmin):
        model = Codigo
        list_display = ['nombre_usuario','nombre_estudio']
        def nombre_usuario(self,instance):
                return instance.usuario.watsapp
        def nombre_estudio(self,instance):
                return instance.estudio.nombre      
admin.site.register(Codigo,CodigoAdmin)
####################################################
        
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = CategoriaForm
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ['nombre']      
admin.site.register(Categoria,CategoriaAdmin)
####################################################



####################################################
class RulesAdmin(admin.ModelAdmin):
    form = EstudiosForm
class EstudiosAdmin(admin.ModelAdmin):
        model = Estudios
        list_display = ['nombre','tipo_de_estudio','fecha_inicio','fecha_final', 'n_muestras']

admin.site.register(Estudios,EstudiosAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = PreguntasForm
class PreguntasAdmin(admin.ModelAdmin):
        model = Preguntas
        list_display = ['nombre_estudio','pregunta']
        
        def nombre_estudio(self,instance):
                return instance.estudio.nombre

admin.site.register(Preguntas,PreguntasAdmin)
####################################################

####################################################
class RulesAdmin(admin.ModelAdmin):
    form = OpcionesForm
class OpcionesAdmin(admin.ModelAdmin):
        model = Opciones
        list_display = ['nombre_pregunta','pregunta']
        
        def nombre_pregunta(self,instance):
                return instance.pregunta.pregunta

admin.site.register(Opciones,OpcionesAdmin)
####################################################


####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Opciones_acumuladasForm
class Opciones_acumuladasAdmin(admin.ModelAdmin):
        model = Opciones_acumuladas
        list_display = ['nombre_pregunta','pregunta']
        
        def nombre_pregunta(self,instance):
                return instance.pregunta.pregunta

admin.site.register(Opciones_acumuladas,Opciones_acumuladasAdmin)
####################################################


####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Cuestionario_temporalForm
class Cuestionario_temporalAdmin(admin.ModelAdmin):
        model = Cuestionario_temporal
        list_display = ['nombre_estudio','respuesta_1','respuesta_2','respuesta_3','respuesta_4','respuesta_5']
        def nombre_estudio(self,instance):
                return instance.estudio.nombre


admin.site.register(Cuestionario_temporal,Cuestionario_temporalAdmin)
####################################################
####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Cuestionario_principalForm
class Cuestionario_principalAdmin(admin.ModelAdmin):
        model = Cuestionario_principal
        list_display = ['nombre_estudio','respuesta_1','respuesta_2','respuesta_3','respuesta_4','respuesta_5']
        def nombre_estudio(self,instance):
                return instance.estudio.nombre


admin.site.register(Cuestionario_principal,Cuestionario_principalAdmin)
####################################################


####################################################
class RulesAdmin(admin.ModelAdmin):
    form = Configuracion_sistemaForm
class Configuracion_sistemaAdmin(admin.ModelAdmin):
    model = Configuracion_sistema
    list_display = ['n_visitas','mensaje_bienvenida']   
admin.site.register(Configuracion_sistema,Configuracion_sistemaAdmin)
####################################################
