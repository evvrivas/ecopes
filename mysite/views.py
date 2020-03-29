#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic import View
from django import get_version
from django.http import HttpResponse

class Index(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Running Django ' + str(get_version()) + " on OpenShift")


from django.template.loader import get_template
from django.template import Context

from django.template import RequestContext, loader

from django.http import HttpResponse
import datetime
#from datetime import date
#from datetime import datetime



#from books.models import Publisher
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
#from miPagina.books.models import Book
from mysite.settings import MEDIA_URL


from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.contrib.auth.decorators import login_required



from mysite.forms import *
from mysite.datos_artetronica.models import *


from django.contrib.auth.models import User  
from django.core.mail import send_mail
#from templates import *
from django.db.models import Q



from django.db import connection

from random import sample
from collections import Counter


from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import *

##########################
import numpy as np
import matplotlib.pyplot as plt
#################################
import pylab as pl

def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect("/")
       
#@login_required
def pagina_principal(request):   
                         
        return render(request,'principal.html',locals())  
                          
def informacion(request):  
  return render(request,'informacion.html',locals())   
                                     

def crear_usuario(request): 
        #!/usr/bin/python
        # -*- coding: latin-1 -*-       

        import os, sys
       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
               
              
                    form = UserProfileForm(request.POST,request.FILES)                      
                    
                    if form.is_valid() :                        
                            
                            watsapp = form.cleaned_data['watsapp']
                            contra = form.cleaned_data['clave'] 

                            user = User.objects.create_user(username=watsapp, password=contra)
                            user.save()                             
                                                      
                            #usuario = form.save(commit=False)
                            #usuario.id_usuario = user.username # Set the user object here
                            #usuario.save() # Now you can send it to DB
                            
                            form.save() 

                            
                            connection.close()
                            return render(request,'confirmar.html',locals())                  
                

        else:            
                         
                         form=UserProfileForm()
        connection.close()                  
        return render(request,'formulario_ingreso.html',locals()) 


@login_required
def editar_usuario(request):
             usuario=UserProfile.objects.get(watsapp=request.user.username)
             tipo_usuario=usuario.tipo_usuario   
              
             f = UserProfile.objects.get(watsapp=request.user.username)           
             
             if request.method == 'POST':
                  
                  form = UserProfileForm(request.POST,request.FILES,instance=f)
             
                  if form.is_valid():

                          contra = form.cleaned_data['clave']
                          watsapp = form.cleaned_data['watsapp']                       

                          user = User.objects.get(username=request.user.username)
                          user.set_password(contra)
                          user.username=watsapp                          

                          user.save()

                          #usu=form.save(commit=False)
                          #usu.id_usuario = request.user.username
                          #usu.save() # Guardar los datos en la base de datos 
                          
                          form.save() 
                            
                          connection.close()
                          return render(request,'confirmar.html',locals())             
                  
             else:
                  
                  form = UserProfileForm(instance=f)               
         
             connection.close()
             #return render_to_response('formulario.html', locals(),context_instance=RequestContext(request))
           
             return render(request,'formulario_ingreso.html',locals())


def poner_lista_de_estudios(request,bandera):

        usuario=UserProfile.objects.get(watsapp=request.user.username)
        tipo_usuario=usuario.tipo_usuario

        usuario_actual=request.user.username
        lista_de_codigos=Codigo.objects.filter(usuario__watsapp=usuario_actual)
        
        vector_de_estudios_publicos=[]

        vector_de_estudios_publicos_habilitados=[]
        vector_de_estudios_publicos_deshabilitados=[]
        
        vector_de_estudios_de_pago_habilitados=[]
        vector_de_estudios_de_pago_deshabilitados=[]
        
        vector_de_estudios_privados_habilitados=[]
        
          
        if bandera=="TODOS":
                 

                estudios=Estudios.objects.filter(tipo_de_estudio="PUBLICO")
                #vector_de_estudios_publicos=estudios
                if estudios.count()>0:


                    if lista_de_codigos.count()==0:
                        vector_de_estudios_publicos_deshabilitados=estudios
                    else:
                        for i in estudios:
                            try:
                                x=lista_de_codigos.get(estudio=i)

                                if x.estado_del_estudio=="ACTIVO":
                                          vector_de_estudios_publicos_habilitados.append(i)
                                else:
                                          vector_de_estudios_publicos_deshabilitados.append(i)
                                      
                            except:
                              vector_de_estudios_publicos_deshabilitados.append(i)













                estudios=Estudios.objects.filter(tipo_de_estudio="DE_PAGO")
                
                if estudios.count()>0:


                    if lista_de_codigos.count()==0:
                        vector_de_estudios_de_pago_deshabilitados=estudios
                    else:
                        for i in estudios:
                            try:
                                x=lista_de_codigos.get(estudio=i)

                                if x.estado_del_estudio=="ACTIVO":
                                          vector_de_estudios_de_pago_habilitados.append(i)
                                else:
                                          vector_de_estudios_de_pago_deshabilitados.append(i)
                                      
                            except:
                              vector_de_estudios_de_pago_deshabilitados.append(i)

               
                estudios=Estudios.objects.filter(tipo_de_estudio="PRIVADO")
                if estudios.count()>0:

                    if lista_de_codigos.count()==0:
                      vector_de_estudios_privados_deshabilitados=estudios
                    
                    else:
                        for i in estudios:
                          try:  
                                    x=lista_de_codigos.get(estudio=i)

                                    if x.estado_del_estudio=="ACTIVO":
                                              vector_de_estudios_de_pago_habilitados.append(i)
                                    else:
                                              vector_de_estudios_de_pago_deshabilitados.append(i)
                          except:
                              vector_de_estudios_de_pago_deshabilitados.append(i)


        elif bandera=="PUBLICO":
                estudios=Estudios.objects.filter(tipo_de_estudio="PUBLICO")
                if estudios.count()>0:
                    if lista_de_codigos.count()==0:
                        vector_de_estudios_publicos_deshabilitados=estudios
                    else:
                        for i in estudios:
                            try:
                                x=lista_de_codigos.get(estudio=i)

                                if x.estado_del_estudio=="ACTIVO":
                                          vector_de_estudios_publicos_habilitados.append(i)
                                else:
                                          vector_de_estudios_publicos_deshabilitados.append(i)
                                      
                            except:
                              vector_de_estudios_publicos_deshabilitados.append(i)



        





        elif bandera=="DE_PAGO":
                estudios=Estudios.objects.filter(tipo_de_estudio="DE_PAGO")
                if estudios.count()>0:

                    if lista_de_codigos.count()==0:
                        vector_de_estudios_de_pago_deshabilitados=estudios
                    else:
                        for i in estudios:

                            try:
                                x=lista_de_codigos.get(estudio=i)

                                if x.estado_del_estudio=="ACTIVO":
                                          vector_de_estudios_de_pago_habilitados.append(i)
                                else:
                                          vector_de_estudios_de_pago_deshabilitados.append(i)
                            except:
                              vector_de_estudios_de_pago_deshabilitados.append(i)  

                   
        elif bandera=="PRIVADO":
                estudios=Estudios.objects.filter(tipo_de_estudio="PRIVADO")
                if estudios.count()>0:

                    if lista_de_codigos.count()==0:
                      vector_de_estudios_privados_deshabilitados=estudios
                    
                    else:
                        
                        for i in estudios:
                            try:
                                    x=lista_de_codigos.get(estudio=i)

                                    if x.estado_del_estudio=="ACTIVO":
                                              vector_de_estudios_de_pago_habilitados.append(i)
                                    else:
                                              vector_de_estudios_de_pago_deshabilitados.append(i)
                            except:
                              vector_de_estudios_de_pago_deshabilitados.append(i)  
      
  
                      
        else:
               pass
                              
     
    
             

        return render(request,'lista_de_estudios.html',locals())
     


def poner_cuestionario(request,id_estudio):

      vector_de_opciones=[]
      usuario=UserProfile.objects.get(watsapp=request.user.username)
      tipo_usuario=usuario.tipo_usuario
      
      
      estudio_actual=Estudios.objects.get(id=id_estudio)
      las_preguntas=Preguntas.objects.filter(estudio=estudio_actual)

      
      for i in las_preguntas:
           
            las_opciones=Opciones.objects.filter(pregunta=i)
            vector_de_opciones.append(las_opciones)
            
      connection.close()
      return render(request,'cuestionario.html',locals()) 




     
     
def agregar_encuesta(request,id_estudio):
    
    if request.POST:
            id_estudio=id_estudio
            vector_de_preguntas=[]
            
            estudio_actual=Estudios.objects.get(id=id_estudio)
            las_preguntas=Preguntas.objects.filter(estudio=estudio_actual)      
            
            for i in las_preguntas:
                  
                  las_opciones=Opciones.objects.filter(pregunta=i)
                  vector_de_preguntas.append(las_opciones)           
           
            respuesta_1=""
            respuesta_2=""
            respuesta_3=""
            respuesta_4=""
            respuesta_5=""
            respuesta_6=""
            respuesta_7=""
            respuesta_8=""
            respuesta_9=""
            respuesta_10=""

            respuesta_11=""
            respuesta_12=""
            respuesta_13=""
            respuesta_14=""
            respuesta_15=""
            respuesta_16=""
            respuesta_17=""
            respuesta_18=""
            respuesta_19=""
            respuesta_20=""

            respuesta_21=""
            respuesta_22=""
            respuesta_23=""
            respuesta_24=""
            respuesta_25=""
            respuesta_26=""
            respuesta_27=""
            respuesta_28=""
            respuesta_29=""
            respuesta_30=""

            respuesta_31=""
            respuesta_32=""
            respuesta_33=""
            respuesta_34=""
            respuesta_35=""
            respuesta_36=""
            respuesta_37=""
            respuesta_38=""
            respuesta_39=""
            respuesta_40=""

            respuesta_41="" 
            respuesta_42=""
            respuesta_43=""
            respuesta_44=""
            respuesta_45=""
            respuesta_46=""
            respuesta_47=""
            respuesta_48=""
            respuesta_49=""
            respuesta_50=""

            seleccionadas=[]
            x=1 

            for i in vector_de_preguntas:
              for k in i:
                 opcion_s = request.POST.get(k.pregunta.pregunta)
                                  
                 if x==1:
                    respuesta_1=opcion_s
                 elif x==2:
                    respuesta_2=opcion_s
                 elif x==3:
                    respuesta_3=opcion_s
                 elif x==4:
                    respuesta_4=opcion_s
                 elif x==5:
                    respuesta_5=opcion_s
                 elif x==6:
                    respuesta_6=opcion_s
                 elif x==7:
                    respuesta_7=opcion_s
                 elif x==8:
                    respuesta_8=opcion_s
                 elif x==9:
                    respuesta_9=opcion_s
                 elif x==10:
                    respuesta_10=opcion_s
                 elif x==11:
                    respuesta_11=opcion_s
                 elif x==12:
                    respuesta_12=opcion_s
                 elif x==13:
                    respuesta_13=opcion_s
                 elif x==14:
                    respuesta_14=opcion_s
                 elif x==15:
                    respuesta_15=opcion_s
                 elif x==16:
                    respuesta_16=opcion_s
                 elif x==17:
                    respuesta_17=opcion_s
                 elif x==18:
                    respuesta_18=opcion_s
                 elif x==19:
                    respuesta_19=opcion_s
                 elif x==20:
                    respuesta_20=opcion_s
                 elif x==21:
                    respuesta_21=opcion_s
                 elif x==22:
                    respuesta_22=opcion_s
                 elif x==23:
                    respuesta_23=opcion_s
                 elif x==24:
                    respuesta_24=opcion_s
                 elif x==25:
                    respuesta_25=opcion_s
                 elif x==26:
                    respuesta_26=opcion_s
                 elif x==27:
                    respuesta_27=opcion_s
                 elif x==28:
                    respuesta_28=opcion_s
                 elif x==29:
                    respuesta_29=opcion_s
                 elif x==30:
                    respuesta_30=opcion_s
                 elif x==31:
                    respuesta_31=opcion_s
                 elif x==32:
                    respuesta_32=opcion_s
                 elif x==33:
                    respuesta_33=opcion_s
                 elif x==34:
                    respuesta_34=opcion_s
                 elif x==35:
                    respuesta_35=opcion_s
                 elif x==36:
                    respuesta_36=opcion_s
                 elif x==37:
                    respuesta_37=opcion_s
                 elif x==38:
                    respuesta_38=opcion_s
                 elif x==39:
                    respuesta_39=opcion_s
                 elif x==40:
                    respuesta_40=opcion_s
                 elif x==41:
                    respuesta_41=opcion_s
                 elif x==42:
                    respuesta_42=opcion_s
                 elif x==43:
                    respuesta_43=opcion_s
                 elif x==44:
                    respuesta_44=opcion_s
                 elif x==45:
                    respuesta_45=opcion_s
                 elif x==46:
                    respuesta_46=opcion_s
                 elif x==47:
                    respuesta_47=opcion_s
                 elif x==48:
                    respuesta_48=opcion_s
                 elif x==49:
                    respuesta_49=opcion_s
                 elif x==50:
                    respuesta_50=opcion_s   
                 else:
                    pass

                 break
              x=x+1   


            usuario_actual=request.user.username

            codigo=Codigo.objects.get(usuario__watsapp=usuario_actual)
            a=codigo.cantidad_muestras_realizadas
            a=a+1
            codigo.cantidad_muestras_realizadas=a
            codigo.save()  


            fecha= datetime.datetime.now()
         

            p1=Cuestionario_temporal(estudio=estudio_actual,respuesta_1=respuesta_1,respuesta_2=respuesta_2,respuesta_3=respuesta_3,respuesta_4=respuesta_4,respuesta_5=respuesta_5,
                                      respuesta_6=respuesta_6,respuesta_7=respuesta_7,respuesta_8=respuesta_8,respuesta_9=respuesta_9,respuesta_10=respuesta_10,
                                      respuesta_11=respuesta_11,respuesta_12=respuesta_12,respuesta_13=respuesta_13,respuesta_14=respuesta_14,respuesta_15=respuesta_15,
                                      respuesta_16=respuesta_16,respuesta_17=respuesta_17,respuesta_18=respuesta_18,respuesta_19=respuesta_19,respuesta_20=respuesta_20,
                                      respuesta_21=respuesta_21,respuesta_22=respuesta_22,respuesta_23=respuesta_23,respuesta_24=respuesta_24,respuesta_25=respuesta_25,
                                      respuesta_26=respuesta_26,respuesta_27=respuesta_27,respuesta_28=respuesta_28,respuesta_29=respuesta_29,respuesta_30=respuesta_30,
                                      respuesta_31=respuesta_31,respuesta_32=respuesta_32,respuesta_33=respuesta_33,respuesta_34=respuesta_34,respuesta_35=respuesta_35,
                                      respuesta_36=respuesta_36,respuesta_37=respuesta_37,respuesta_38=respuesta_38,respuesta_39=respuesta_39,respuesta_40=respuesta_40,
                                      respuesta_41=respuesta_41,respuesta_42=respuesta_42,respuesta_43=respuesta_43,respuesta_44=respuesta_44,respuesta_45=respuesta_45,
                                      respuesta_46=respuesta_46,respuesta_47=respuesta_47,respuesta_48=respuesta_48,respuesta_49=respuesta_49,respuesta_50=respuesta_50,encuestador=usuario_actual,fecha_de_ingreso=fecha) 
                #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
            p1.save()

            p1=Cuestionario_principal(estudio=estudio_actual,respuesta_1=respuesta_1,respuesta_2=respuesta_2,respuesta_3=respuesta_3,respuesta_4=respuesta_4,respuesta_5=respuesta_5,
                                      respuesta_6=respuesta_6,respuesta_7=respuesta_7,respuesta_8=respuesta_8,respuesta_9=respuesta_9,respuesta_10=respuesta_10,
                                      respuesta_11=respuesta_11,respuesta_12=respuesta_12,respuesta_13=respuesta_13,respuesta_14=respuesta_14,respuesta_15=respuesta_15,
                                      respuesta_16=respuesta_16,respuesta_17=respuesta_17,respuesta_18=respuesta_18,respuesta_19=respuesta_19,respuesta_20=respuesta_20,
                                      respuesta_21=respuesta_21,respuesta_22=respuesta_22,respuesta_23=respuesta_23,respuesta_24=respuesta_24,respuesta_25=respuesta_25,
                                      respuesta_26=respuesta_26,respuesta_27=respuesta_27,respuesta_28=respuesta_28,respuesta_29=respuesta_29,respuesta_30=respuesta_30,
                                      respuesta_31=respuesta_31,respuesta_32=respuesta_32,respuesta_33=respuesta_33,respuesta_34=respuesta_34,respuesta_35=respuesta_35,
                                      respuesta_36=respuesta_36,respuesta_37=respuesta_37,respuesta_38=respuesta_38,respuesta_39=respuesta_39,respuesta_40=respuesta_40,
                                      respuesta_41=respuesta_41,respuesta_42=respuesta_42,respuesta_43=respuesta_43,respuesta_44=respuesta_44,respuesta_45=respuesta_45,
                                      respuesta_46=respuesta_46,respuesta_47=respuesta_47,respuesta_48=respuesta_48,respuesta_49=respuesta_49,respuesta_50=respuesta_50,encuestador=usuario_actual,fecha_de_ingreso=fecha) 
                #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
            p1.save()


            

            #tabla_datos=Cuestionario_temporal.objects.all()
            connection.close()
            return render(request,'confirmar_encuesta.html',locals())             

    connection.close()
    return render(request,'principal.html',locals())



def actualizar_previo_a_graficar(request,id_estudio):     
         
      id_estudio=id_estudio
      estudio_actual=Estudios.objects.get(id=id_estudio)
      las_preguntas=Preguntas.objects.filter(estudio=estudio_actual)    

      datos_temporales=Cuestionario_temporal.objects.filter(estudio__id=id_estudio)
      
      texto=[field.name for field in Cuestionario_temporal._meta.get_fields()]
                 
      i=2  
      
      for j in las_preguntas:
                        las_opciones=Opciones.objects.filter(pregunta=j)
                        lista_respuesta=datos_temporales.values_list(texto[i], flat=True) 

                        list_freq= (Counter(lista_respuesta))
                        vector_de_acumulados=[]                        
                        for k in las_opciones:
                              x=k.opcion
                              repeticiones=list_freq[x]
                              vector_de_acumulados.append(repeticiones)

                              valor_actual=k.cantidad
                              k.cantidad=valor_actual+repeticiones
                              k.save()                                                          
                                                                                
                        i=i+1
                        guardar_en_acumulados(vector_de_acumulados,j)

      Cuestionario_temporal.objects.filter(estudio__id=id_estudio).delete()

      
      if estudio_actual.confianza=="75%":
        c=1.15
      elif estudio_actual.confianza=="80%":
        c=1.28
      elif estudio_actual.confianza=="85%":
        c=1.44
      elif estudio_actual.confianza=="90%":
        c=1.65
      elif estudio_actual.confianza=="95%":
        c=1.96
      elif estudio_actual.confianza=="95.5%":
        c=2.0
      elif estudio_actual.confianza=="99%":
        c=2.58
      else:
        c=1.15



      n=estudio_actual.universo
      N=estudio_actual.n_muestras         
      k=c
      p=0.5
      q=0.5    

      e=k*sqrt(p*q*(N/n -1)/(N-1) )
      print("error",e)
      ee=str(round(e, 1))
      estudio_actual.error=ee
      N=N+1     
      estudio_actual.n_muestras=N
      estudio_actual.fecha_ultima_actualizacion= datetime.datetime.now()

      estudio_actual.save()      
      return render(request,'confirmar_encuesta.html',locals())


def guardar_en_acumulados(vector_de_acumulados,pregunta_actual):
         
             #keys = list_freq.keys();
             #values = list_freq.values()
         
             #for key, value in list_freq.items():
                 #print(key, " has count ", value)
                 #vector_de_acumulados.append(value)
             fecha=datetime.datetime.now()
             va=vector_de_acumulados
             t=len(vector_de_acumulados)
             a=0
             if t==1:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0])
             elif t==2:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1])
             elif t==3:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2])
             elif t==4:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3])
             elif t==5:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4])
             elif t==6:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5])
             elif t==7:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6])
             elif t==8:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6],opcion_8=va[7])
             elif t==9:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6],opcion_8=va[7],opcion_9=va[8])
             elif t==10:
                 p=Opciones_acumuladas(fecha_de_actualizacion=fecha,pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6],opcion_8=va[7],opcion_9=va[8],opcion_10=va[9])

             else:
                 a=1

             if a==0:
                  p.save() 



def pagina_de_analisis(request, id_pregunta,id_pregunta_de_cruze,bandera):

    pregunta=Preguntas.objects.get(id=id_pregunta)
    id_estudio=pregunta.estudio.id

    lista_de_opciones=Opciones.objects.filter(pregunta__pregunta=pregunta.pregunta) 
    
    nombre_de_pregunta=pregunta.pregunta   
    id_pregunta=id_pregunta
    bandera=bandera
    id_pregunta_de_cruze=id_pregunta_de_cruze
    pregunta_de_cruze=Preguntas.objects.get(id=id_pregunta_de_cruze)
    lista_de_opciones_de_cruze=Opciones.objects.filter(pregunta__pregunta=pregunta_de_cruze.pregunta) 
   


    
   
    #tabla_resultados=Cuestionario_principal.objects.filter(estudio__nombre=pregunta.estudio.nombre)
    return render(request,'pagina_de_analisis.html',locals())

def informacion_del_estudio(request,id_estudio):
    estudio=Estudios.objects.get(id=id_estudio)
    preguntas=preguntas.objects.filter(estudio__id=id_estudio)

    return render(request,'informacion_del_estudio.html',locals())



def hacer_grafico_de_barras(request,id_pregunta):
        vector_de_opciones=[]
        vector_de_repeticiones=[]
        opci=Opciones.objects.filter(pregunta__id=id_pregunta)       
      
        x=1
        for i in opci:
            xx=str(x)
            vector_de_opciones.append(xx)
            vector_de_repeticiones.append(i.cantidad)
            x=x+1    

        total=sum(vector_de_repeticiones)
        a=np.array(vector_de_repeticiones)
        b=a*100/total
        b=round(b,2)
  
        X= np.arange(len(vector_de_opciones))
        X=X+1
        
        Y1 = np.asarray(b)  
     
               
        f=plt.figure()
        f.set_size_inches(3,6)
       
        #plt.gca().set_yscale('log')

       
        bar_width = 0.45
        plt.bar(X, Y1, bar_width, color='b')

               
      
        #z=0 
        #for x, y in zip(X, Y1):
        #    plt.text(x, y+1 ,str(y)+ "\n"+vector_de_opciones[z], ha='center', va= 'bottom')
        #    z=z+1
        z=0 
        for x, y in zip(X, Y1):
            plt.text(x, y ,str(y), ha='center', va= 'bottom')
            z=z+1
 
      
        plt.xlabel('\nOpciones disponibles a esta pregunta')
        plt.ylabel('Porcentaje (respuestas) /opcion ')
        titulo=""
        plt.title(titulo)
        plt.xticks(X)

        subplots_adjust(left=0.21)
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")




def hacer_grafico_de_pastel(request,id_pregunta):
        vector_de_opciones=[]
        vector_de_repeticiones=[]
        opci=Opciones.objects.filter(pregunta__id=id_pregunta)       
      

        x=1
        for i in opci:
            xx=str(x)
            vector_de_opciones.append(xx)
            vector_de_repeticiones.append(i.cantidad)
            x=x+1    

        total=sum(vector_de_repeticiones)
        a=np.array(vector_de_repeticiones)
        b=a*100/total
  
        X= np.arange(len(vector_de_opciones))
        X=X+1
        
        Y1 = np.asarray(b)  
     
               
        f=plt.figure()
        f.set_size_inches(3,6)


        #desfase = (0.1, 0, 0, 0, 0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

        color=["red","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","black"] 
      
        
        plt.pie(Y1, labels=vector_de_opciones, autopct="%0.1f %%", colors=color)
        plt.axis("equal")
        plt.show()      
              
      
        plt.xlabel('\nOpciones disponibles a esta pregunta')
        plt.ylabel('Cantidad de respuestas/opcion ')
        titulo=""
        plt.title(titulo)
        plt.xticks(())

        subplots_adjust(left=0.21)
      

        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  

        f.clear()
        
        return HttpResponse (buffer.getvalue(), content_type="Image/png")


def hacer_grafico_de_secuencia(request,id_pregunta):
       
       opcion_secuencial=Opciones_acumuladas.objects.filter(pregunta__id=id_pregunta)
       texto=[field.name for field in Opciones_acumuladas._meta.get_fields()]

       nombre_opcion=Opciones.objects.filter(pregunta__id=id_pregunta)
       
       vector_de_secuencias=[]

            
       x=len(nombre_opcion)+2
       for i in range(3,x):
            vector1=opcion_secuencial.values_list(texto[i], flat=True)
            vector2=vector1
            vector3=[]

            for j in range(len(vector2)):
                if j ==0:
                    
                    vector3.append(vector2[j])
                
                else:
                    b=j-1

                    c=vector2[j]+vector3[b]
                    vector3.append(c)
                

            #total=sum(vector3)
            #vector33=vector3*100/total
            total=sum(vector3)            
            vector22=np.array(vector3)
            vector2=vector22*100/total 

            vector_de_secuencias.append(vector2)
        
       X= np.arange(len(vector2))
       fecha=opcion_secuencial.values_list("fecha_de_actualizacion", flat=True)     
       anios=[]       
       for i in  fecha:
            an=i.strftime('%d%m%Y') 
            anios.append(an)
       #X= np.arange(len(fecha))
       
       #barh(pos,datos,align = 'center')
       f=plt.figure()
       f.set_size_inches(3,6)
       color=["red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow"] 
       #titulo_color=[", 1-red",", 2-black",", 3-blue",", 4-green","5, -orange",", 6-gray",", 7-yelow",", 8-red",", 9-black",", 10-blue",", 11-green",", 12-orange",", 13-gray",", 14-yelow",", 15-red",", 16-black",", 17-blue",", 18-green",", 19-orange",", 20-gray",", 21-yelow"] 
       titulo_color=[", 1-rojo",", 2-negro",", 3-azul",", 4-verde","5-anaranjdo",", 6-gris",", 7-amarillo",", 8-rojo",", 9-negro",", 10-azul",", 11-verde",", 12-anaranjado",", 13-gris",", 14-amarillo",", 15-rojo",", 16-negro",", 17-azul",", 18-verde",", 19-anaranjado",", 20-gris",", 21-amarillo"] 

       b=0

       titulo=""
       for i in vector_de_secuencias:
                plt.plot(anios,i, color[b],"o-")
                t_color=titulo_color[b]
                titulo=titulo+t_color
                b=b+1
               

       plt.grid()     
        

       plt.ylim(0, 100)    
       plt.ylabel('PREFERENCIAS')

       plt.xticks(rotation='vertical',size="small")
       plt.xlabel('Fecha de actualización ')

       #titulo="preferencias "
       #plt.xticks(())
       #plt.yticks()
      
       #titulo="Tendencia del las preferencias\n"+" fml "+str(fml)+ "%    "+  "gan "+str(gan)+ "%    "+"vamo "+str(vamo)+ "%    "+"alian "+str(aaa)+ "%" +  "NS+NR "+str(ns_nr)+ "%"
       plt.title(titulo)  
                    
       subplots_adjust(left=0.21)      

       buffer = io.BytesIO()
       canvas = pylab.get_current_fig_manager().canvas
       canvas.draw()        
       graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
       graphIMG.save(buffer, "PNG")
       pylab.close()  
       f.clear()
        
       return HttpResponse (buffer.getvalue(), content_type="Image/png")


def hacer_grafico_de_tendencia(request,id_pregunta):
       
       opcion_secuencial=Opciones_acumuladas.objects.filter(pregunta__id=id_pregunta)
       texto=[field.name for field in Opciones_acumuladas._meta.get_fields()]

       nombre_opcion=Opciones.objects.filter(pregunta__id=id_pregunta)
       
       vector_de_secuencias=[]

       x=len(nombre_opcion)+2
       for i in range(3,x):
            vector1=opcion_secuencial.values_list(texto[i], flat=True)
            
            total=sum(vector1)            
            vector22=np.array(vector1)
            vector2=vector22*100/total
                        
            vector_de_secuencias.append(vector2)
        
       X= np.arange(len(vector2))

       fecha=opcion_secuencial.values_list("fecha_de_actualizacion", flat=True)     
       anios=[]       
       for i in  fecha:
            an=i.strftime('%d%m%Y') 
            anios.append(an)
       #X= np.arange(len(fecha))





       #print(vector_de_secuencias)
       #barh(pos,datos,align = 'center')
       f=plt.figure()
       f.set_size_inches(3,6)
       color=["red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow"] 
       titulo_color=[", 1-rojo",", 2-negro",", 3-azul",", 4-verde","5-anaranjdo",", 6-gris",", 7-amarillo",", 8-rojo",", 9-negro",", 10-azul",", 11-verde",", 12-anaranjado",", 13-gris",", 14-amarillo",", 15-rojo",", 16-negro",", 17-azul",", 18-verde",", 19-anaranjado",", 20-gris",", 21-amarillo"] 

       b=0
       titulo=""
       for i in vector_de_secuencias:
                plt.plot(anios,i, color[b],"o-")
                t_color=titulo_color[b]
                titulo=titulo+t_color
                b=b+1

       plt.grid()    
    
           
       plt.ylabel('PREFERENCIAS')
       #titulo="Variacion del las preferencias"
       plt.xticks(rotation='vertical',size="small")
       plt.xlabel('Fecha de actualización ')
      
       #titulo="Tendencia del las preferencias\n"+" fml "+str(fml)+ "%    "+  "gan "+str(gan)+ "%    "+"vamo "+str(vamo)+ "%    "+"alian "+str(aaa)+ "%" +  "NS+NR "+str(ns_nr)+ "%"
       plt.title(titulo)  
                    
       subplots_adjust(left=0.21)      

       buffer = io.BytesIO()
       canvas = pylab.get_current_fig_manager().canvas
       canvas.draw()        
       graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
       graphIMG.save(buffer, "PNG")
       pylab.close()  
       f.clear()
        
       return HttpResponse (buffer.getvalue(), content_type="Image/png")





def habilitar_estudio(request,id_del_estudio):      
       
        usuario_actual=request.user.username
        perfil_usuario_actual=UserProfile.objects.get(watsapp=usuario_actual)
        estudio_actual=Estudios.objects.get(id=id_del_estudio)
        precio_de_la_muestra=estudio_actual.costo_por_muestra


        existe=Codigo.objects.filter(usuario=perfil_usuario_actual,estudio=estudio_actual).count()
        
        if existe>0:

            return render(request,'solicitud_de_suscripcion.html',locals())

        else:
            date=datetime.datetime.now()  
            nuevo=Codigo(usuario=perfil_usuario_actual,estudio=estudio_actual,solicitud_de_activacion="ACTIVAR",estado_del_estudio="DESACTIVADO",cantidad_muestras_asignadas=0,cantidad_muestras_realizadas=0,costo_por_muestra=precio_de_la_muestra,fecha_inicio=date,comodin=0)
            nuevo.save()

            return render(request,'solicitud_de_suscripcion.html',locals())  


def ver_mis_numeros(request):
      usuario_actual=request.user.username
      perfil_del_usuario=UserProfile.objects.get(watsapp=usuario_actual)
      tipo_usuario=perfil_del_usuario.tipo_usuario

      listado_de_mis_estudios=Codigo.objects.filter(usuario=perfil_del_usuario)
    

      return render(request,'ver_mis_numeros.html',locals())

def filtro_casero(id_del_estudio,x,opcion):

      if x==2:
          arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_1=opcion)
      elif x==3:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_2=opcion)
      elif x==4:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_3=opcion)
      elif x==5:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_4=opcion)
      elif x==6:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_5=opcion)
      elif x==7:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_6=opcion)
      elif x==8:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_7=opcion)
      elif x==9:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_8=opcion)
      elif x==10:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_9=opcion)
      elif x==11:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_10=opcion)
      elif x==12:
          arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_11=opcion)
      elif x==13:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_12=opcion)
      elif x==14:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_13=opcion)
      elif x==15:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_14=opcion)
      elif x==16:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_15=opcion)
      elif x==17:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_16=opcion)
      elif x==18:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_17=opcion)
      elif x==19:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_18=opcion)
      elif x==20:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_19=opcion)
      elif x==21:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_20=opcion)
      if x==22:
          arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_21=opcion)
      elif x==23:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_22=opcion)
      elif x==24:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_23=opcion)
      elif x==25:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_24=opcion)
      elif x==26:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_25=opcion)
      elif x==27:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_26=opcion)
      elif x==28:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_27=opcion)
      elif x==29:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_28=opcion)
      elif x==30:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_29=opcion)
      elif x==31:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_30=opcion)
      elif x==32:
          arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_31=opcion)
      elif x==33:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_32=opcion)
      elif x==34:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_33=opcion)
      elif x==35:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_34=opcion)
      elif x==36:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_35=opcion)
      elif x==37:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_36=opcion)
      elif x==38:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_37=opcion)
      elif x==39:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_38=opcion)
      elif x==40:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_39=opcion)
      elif x==41:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_40=opcion)
      elif x==42:
          arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_41=opcion)
      elif x==43:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_42=opcion)
      elif x==44:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_43=opcion)
      elif x==45:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_44=opcion)
      elif x==46:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_45=opcion)
      elif x==47:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_46=opcion)
      elif x==48:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_47=opcion)
      elif x==49:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_48=opcion)
      elif x==50:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_49=opcion)
      elif x==11:
        arreglo_filtrado_con_la_opcion=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio).filter(respuesta_50=opcion)
      else: 
        pass
      return arreglo_filtrado_con_la_opcion 

def filtro_casero_2(vector,x,opcion):
      if x==2:
          arreglo_filtrado_con_la_opcion=vector.filter(respuesta_1=opcion).count()
      elif x==3:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_2=opcion).count()
      elif x==4:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_3=opcion).count()
      elif x==5:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_4=opcion).count()
      elif x==6:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_5=opcion).count()
      elif x==7:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_6=opcion).count()
      elif x==8:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_7=opcion).count()
      elif x==9:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_8=opcion).count()
      elif x==10:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_9=opcion).count()
      elif x==11:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_10=opcion).count()
      elif x==12:
          arreglo_filtrado_con_la_opcion=vector.filter(respuesta_11=opcion).count()
      elif x==13:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_12=opcion).count()
      elif x==14:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_13=opcion).count()
      elif x==15:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_14=opcion).count()
      elif x==16:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_15=opcion).count()
      elif x==17:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_16=opcion).count()
      elif x==18:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_17=opcion).count()
      elif x==19:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_18=opcion).count()
      elif x==20:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_19=opcion).count()
      elif x==21:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_20=opcion).count()
      if x==22:
          arreglo_filtrado_con_la_opcion=vector.filter(respuesta_21=opcion).count()
      elif x==23:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_22=opcion).count()
      elif x==24:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_23=opcion).count()
      elif x==25:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_24=opcion).count()
      elif x==26:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_25=opcion).count()
      elif x==27:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_26=opcion).count()
      elif x==28:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_27=opcion).count()
      elif x==29:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_28=opcion).count()
      elif x==30:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_29=opcion).count()
      elif x==31:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_30=opcion).count()
      elif x==32:
          arreglo_filtrado_con_la_opcion=vector.filter(respuesta_31=opcion).count()
      elif x==33:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_32=opcion).count()
      elif x==34:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_33=opcion).count()
      elif x==35:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_34=opcion).count()
      elif x==36:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_35=opcion).count()
      elif x==37:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_36=opcion).count()
      elif x==38:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_37=opcion).count()
      elif x==39:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_38=opcion).count()
      elif x==40:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_39=opcion).count()
      elif x==41:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_40=opcion).count()
      elif x==42:
          arreglo_filtrado_con_la_opcion=vector.filter(respuesta_41=opcion).count()
      elif x==43:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_42=opcion).count()
      elif x==44:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_43=opcion).count()
      elif x==45:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_44=opcion).count()
      elif x==46:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_45=opcion).count()
      elif x==47:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_46=opcion).count()
      elif x==48:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_47=opcion).count()
      elif x==49:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_48=opcion).count()
      elif x==50:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_49=opcion).count()
      elif x==11:
        arreglo_filtrado_con_la_opcion=vector.filter(respuesta_50=opcion).count()
      else: 
        pass
      return arreglo_filtrado_con_la_opcion 


def graficar_cruse_de_datos(request,id_del_estudio,id_pregunta_padre,id_pregunta_hijo):
        pregunta_padre=Preguntas.objects.get(id=id_pregunta_padre)
        pregunta_hijo=Preguntas.objects.get(id=id_pregunta_hijo)

        opci_padre=Opciones.objects.filter(pregunta__id=id_pregunta_padre)
        opci_hijo=Opciones.objects.filter(pregunta__id=id_pregunta_hijo)

        las_preguntas=Preguntas.objects.filter(estudio__id=id_del_estudio)       
        #cuestionario_analisis=Cuestionario_principal.objects.filter(estudio__id=id_del_estudio)
        texto=[field.name for field in Cuestionario_principal._meta.get_fields()]
   
   
        x=2
        vector_padre=[]  
        for i in las_preguntas:

            if i.pregunta==pregunta_padre.pregunta:

              for k in opci_padre:
                  la_opcion=k.opcion

                  arreglo_filtrado_con_la_opcion=filtro_casero(id_del_estudio,x,la_opcion)

                  cantidad=arreglo_filtrado_con_la_opcion.count()
                  vector_1=[la_opcion,cantidad,arreglo_filtrado_con_la_opcion]
                  vector_padre.append(vector_1)
                  
              break      

            x=x+1


        x=2
       
        vector_conteo_global=[]
        
        for i in las_preguntas:

            if i.pregunta==pregunta_hijo.pregunta:             

              for v in vector_padre:  
                  vector_conteo_hijo=[]
                  for k in opci_hijo:
                     la_opcion=k.opcion
                     conteo_opcion_hijo=filtro_casero_2(v[2],x,la_opcion)
                     vector_1=[v[0], v[1], la_opcion, conteo_opcion_hijo]                     
                     vector_conteo_hijo.append(vector_1)
                     
                  vector_conteo_global.append(vector_conteo_hijo)
              break        
                   

            x=x+1   
        ########################################################################################
        #########################################################################################
        #########################################################################################
        #vector_conteo_global=[  [["hombre",100,"fmln",20], ["hombre",100,"arena",70], ["hombre",10,"pcn",30]],
        #                        [["Mujer", 50, "fmln",10], ["Mujer",10,"arena",15],   ["Mujer",20,"pcn",25 ]]   ]

        celda=len(vector_conteo_global)
        
        vector_de_graficas=[]
        
        titulos=[]
        x_dato=[]

        for i in  vector_conteo_global[0]:
          x_dato.append(i[2])
                
        for i in vector_conteo_global:            
             
             y=[]
             
             
             for j in i:

                 #v=j[3]*100/j[1]
                 y.append(j[3])
             titulos.append(j[0])
                      

             vector_de_graficas.append(y)
        

        f=plt.figure()
        f.set_size_inches(3,12)
        
        celdas=len(vector_de_graficas)
        fila=1
        tit=0

      
        for i in vector_de_graficas:
            total=sum(i)
            a=np.array(i)
            b=a*100/total
            b=round(b, 2)

            Y1 = np.asarray(b)
            X= np.arange(len(i))
            X=X+1
                        
            plt.subplot(celdas,1,fila)
            fila=fila+1
            bar_width = 0.45
            plt.bar(X, Y1, bar_width, color='b')
            plt.yticks()
            plt.xticks()
            z=0 
            for x, y in zip(X, Y1):
                plt.text(x, y ,str(y), ha='center', va= 'center')
                z=z+1
            
            a=titulos[tit]
            plt.title(a)            
            tit=tit+1
                
        #plt.xticks(X)
        buffer = io.BytesIO()
        canvas = pylab.get_current_fig_manager().canvas
        canvas.setPageSize((5*inch, 8*inch))
        canvas.draw()        
        graphIMG = PIL.Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        graphIMG.save(buffer, "PNG")
        pylab.close()  
        f.clear()

        return HttpResponse (buffer.getvalue(), content_type="Image/png")
         


def busqueda(request):     
     bandera="TODOS"  
     if request.POST:
        palabra = request.POST.get('nombre')
             
        usuario=UserProfile.objects.get(watsapp=request.user.username)
        tipo_usuario=usuario.tipo_usuario

        usuario_actual=request.user.username
        lista_de_codigos=Codigo.objects.filter(usuario__watsapp=usuario_actual)
        
        vector_de_estudios_publicos=[]
        vector_de_estudios_publicos_habilitados
        vector_de_estudios_publicos_deshabilitados
        
        vector_de_estudios_de_pago_habilitados=[]
        vector_de_estudios_de_pago_deshabilitados=[]
        
        vector_de_estudios_privados_habilitados=[]



        if bandera=="TODOS":
                 

                estudios=Estudios.objects.filter(tipo_de_estudio="PUBLICO").filter(Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra) | Q(categoria__nombre__icontains=palabra))
                #vector_de_estudios_publicos=estudios
                if estudios.count()>0:


                    if lista_de_codigos.count()==0:
                        vector_de_estudios_publicos_deshabilitados=estudios
                    else:
                        for i in estudios:
                            try:
                                x=lista_de_codigos.get(estudio=i)

                                if x.estado_del_estudio=="ACTIVO":
                                          vector_de_estudios_publicos_habilitados.append(i)
                                else:
                                          vector_de_estudios_publicos_deshabilitados.append(i)
                                      
                            except:
                              vector_de_estudios_publicos_deshabilitados.append(i)



                estudios=Estudios.objects.filter(tipo_de_estudio="DE_PAGO").filter(Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra) | Q(categoria__nombre__icontains=palabra))
                
                if estudios.count()>0:


                    if lista_de_codigos.count()==0:
                        vector_de_estudios_de_pago_deshabilitados=estudios
                    else:
                        for i in estudios:
                            try:
                                x=lista_de_codigos.get(estudio=i)

                                if x.estado_del_estudio=="ACTIVO":
                                          vector_de_estudios_de_pago_habilitados.append(i)
                                else:
                                          vector_de_estudios_de_pago_deshabilitados.append(i)
                                      
                            except:
                              vector_de_estudios_de_pago_deshabilitados.append(i)

               
                estudios=Estudios.objects.filter(tipo_de_estudio="PRIVADO").filter(Q(nombre__icontains=palabra) | Q(descripcion__icontains=palabra) | Q(categoria__nombre__icontains=palabra))
                if estudios.count()>0:

                    if lista_de_codigos.count()==0:
                      vector_de_estudios_privados_deshabilitados=estudios
                    
                    else:
                        for i in estudios:
                          try:  
                                    x=lista_de_codigos.get(estudio=i)

                                    if x.estado_del_estudio=="ACTIVO":
                                              vector_de_estudios_de_pago_habilitados.append(i)
                                    else:
                                              vector_de_estudios_de_pago_deshabilitados.append(i)
                          except:
                              vector_de_estudios_de_pago_deshabilitados.append(i)
                 

        return render(request,'lista_de_estudios.html',locals())
     return render(request,'lista_de_estudios.html',locals())


def manual_de_usuario(request):
    
    return render(request,'manual_de_usuario.html',locals())



class crear_categorias(models.Model):
        
        cat=['POLITICA','ECONOMIA','PHYCOSOCIAL','COMERCIAL', 'ACADEMICO','CIENTIFICA','DEPORTIVA','SOCIAL', 'TECNOLOGICO']
        
        cat=["NACIONAL","AHUACHAPAN","CABAÑAS","CUSCATLAN","CHALATENANGO","LA LIBERTAD","LA PAZ","LA UNION","MORAZAN","SANTA ANA","SAN MIGUEL","SONSONATE","SAN SALVADOR","SAN VICENTE","USULUTAN"]          
        
        for i in cat:
            p1=Estudios(nombre=i)
            p1.save() 
        return render(request,'principal.html',locals())

def crear_estudio_CH5NOV(request):        
              
        import random
        import datetime  
        

        tipo_estudio="PRIVADO"

        nombre_estudio=" 1er. Estudio de Disciplinas deportivas de interes en CH5NOV (Marzo 2020)"
        date=datetime.datetime.now()
        precio=0.15
        precio_suscrip=5.00
        precio_est=300


        descripcion_del_estudio= "Este se realiza entre trabajadores y beneficiarios de la Central Hidroelectrica 5 de Noviembre"
        recomendacion_estudio= "Se recomienda visitar a las personas en sus casas de habitacion y preguntar individualmente a cada persona, sin que terceros intervengann en las respuestas del encuestado. Siempre preguntar si ya alguien les realizo el cuestionario. No hacer 2 veces el cuestionario a la misma persona"
        p1=Estudios(precio_del_estudio=precio_est,precio_por_suscripcion=precio_suscrip,costo_por_muestra=precio,nombre=nombre_estudio,descripcion=descripcion_del_estudio, recomendacion=recomendacion_estudio,fecha_inicio=date,fecha_final=date,fecha_ultima_actualizacion=date,tipo_de_estudio="PUBLICO",n_muestras=300,universo=400,error="1",confianza='1.96')
        p1.save() 


     

        pregunta_est="Cual es su relacionn con CH5NOV "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        ,="Soy Trabajador"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Soy Beneficiari@ Compañer@ de vida "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()
                    
        la_opcion="Soy Beneficiari@ hij@"
        p33=Opciones(pregunta=p21,opcion=la_opcion)
        p33.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Sexo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Masculino"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Femenino "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Rango de edad "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Niño (5-14 años)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Joven (15 a 21 años)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Joven adulto (22- 35 años)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Adulto (35  a 60  años)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Adulto Mayor (60... años)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()






        pregunta_est="Le gustaria participar en estos deportes "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Softball"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Football"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="BasquetBall"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="BoleyBall"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()    






        pregunta_est="En cual de estos otros deportes le gusaria partcipar "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Ping-Pong"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Ajedres"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Billar"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()








        pregunta_est="Si usted fuera autoridad, Que otro deporte propondria a esta central? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Atletismo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Natacion"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
        la_opcion="Carrera de Bicicletas"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()









        pregunta_est="Que lugar propone usted que se habilite para practicar deporte "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Cancha de Football"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Casa de Juegos"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Piscina"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Cancha de Boleyball"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Casa Club (Casa de charlas y conferencias)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Calles internas de la CENTRAL)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Que lo motiva a usted para que llegue a ver practicar a otros deportistas? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Siempre voy, me gusta apoyar"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Voy de ves en cuando, cuando tengo tiempo y energias"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()


        la_opcion="Nada me insentiva, prefiero descanzar"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="llego cuando hay incentivos, Venta de comida"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No me gusta ir"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()






        pregunta_est="Supongamos que el torneo no es de la empresa, Participaria usted si es libre y abierto? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Si, Si apoyaria"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="No, No apoyaria"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        
       
        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        connection.close()
        return render(request,'principal.html',locals())
    
def crear_estudio_FPMA(request):        
              
        import random
        import datetime  
        
# CATEGORIA_ESTUDIO=(
#             ('POLITICO', 'POLITICO'),           
#             ('ECONOMICA', 'ECONOMICA'),
#             ('PHICOSOCIAL', 'PHICOSOCIAL'),
#             ('COMERCIAL', 'COMERCIAL'),
#             ('ACADEMICO', 'ACADEMICO'),
#             ('CIENTIFICA', 'CIENTIFICA'),
#             ('DEPORTIVA', 'DEPORTIVA'),
#             ('SOCIAL', 'SOCIAL'),
#             ('TECNOLOGICO', 'TECNOLOGICO'),
#             )

# TIPO_ESTUDIO=(
#             ('PUBLICO', 'PUBLICO'),         
#             ('DE_PAGO', 'DE_PAGO'),
#             ('PRIVADO', 'PRIVADO'),                         
#             )

# CONFIANZA_NIVEL=(
#             ('75%', '75%'),         
#             ('80%', '80%'),
#             ('85%', '85%'), 
#             ('90%', '90%'),         
#             ('95%', '95%'),
#             ('95.5%', '95.5%'),
#             ('99%', '99%'),                         
#             )
        tipo_estudio="DE_PAGO"

        nombre_estudio="Encuesta: Coyuntura actual y nivel de aceptacion de Diputados y Alcalde del Municipio de Ahuachapán (Marzo 2020)"
        date=datetime.datetime.now()
        precio=0.15
        precio_suscrip=10.00
        precio_est=300


        descripcion_del_estudio= "Este estudio tiene como objetivo medir el nivel de Aceptacion que tienen los actuales diputados residentes en el municipio de Ahuachapan, Asi como la evaluacion de la gestion municipal Actual del Municipio de Ahuachapán"
        recomendacion_estudio= "Se recomienda realizar el estudio a personas mayores de edad, que residan en el municipio de ahuachapán"
        p1=Estudios(precio_del_estudio=precio_est,precio_por_suscripcion=precio_suscrip,costo_por_muestra=precio,nombre=nombre_estudio,descripcion=descripcion_del_estudio, recomendacion=recomendacion_estudio,fecha_inicio=date,fecha_final=date,fecha_ultima_actualizacion=date,tipo_de_estudio="DE_PAGO",n_muestras=300,universo=60000,error="1",confianza='95%')
        p1.save() 

        pregunta_est="Cual es su municipio de Origen"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="AHUACHAPAN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()





        pregunta_est="Cual es su Sexo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Masculino"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Femenino "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Rango de edad "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="18 a 25 años (joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="26 a 35 años (Adulto)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="36 a 60 años (Adulto mayor)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)

        la_opcion="60  a 100 años (Tercera edad)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        pregunta_est="Relaciona Laboral"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Soy o estoy desempleado"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
                    
        la_opcion="Soy empleado Publico"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Soy empleado privado"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Soy empresario independiente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)

        la_opcion="N/S N/R"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()



        pregunta_est="Nivel Academico "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Nunca he estudiado"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
                    
        la_opcion="Estudios Basicos"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Estudio hasta bachillerato o esta en bachillerato"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Tienen estudios tecnicos"
        p32=Opciones(pregunta=p21,opcion=la_opcion)

        la_opcion="Tienen un titulo Universitario o estudio en la Universidad"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Deacuerdo a su persepcion, Cual de estos diputados esta realizando MAL su trabajo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Arturo Magaña (ARENA)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Ricardo Godoy (ARENA)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Isela de Portillo  (FMLN) "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Serafin Orantes (PCN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()    





        pregunta_est="Deacuerdo a su persepcion, Cual de estos diputados esta realizando BIEN su trabajo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Arturo Magaña (ARENA)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Ricardo Godoy (ARENA)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Isela de Portillo  (FMLN) "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Serafin Orantes (PCN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()    



        pregunta_est="Hay un diputado que usted selecciono que realiza bien su trabajo, porque cree eso "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Porque veo su desempeño en el campo legislativo, y veo que promueve leyes en favor de la sociedad"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Porque constantemente veo publicaciones en redes sociales, de su ayuda a la sociedad"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Porque me cae bien, aunque no veo noticias de el, yo creo que hace bien su trabajo"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Es una buena persona y yo vote por el."
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr No seleccione a ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()








        pregunta_est="Con respecto a los Diputados. Cual de estas personas cree usted que debe reelegirse en el cargo?? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Arturo Magaña (ARENA)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Ricardo Godoy (ARENA)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
        la_opcion="Isela de Portillo (FMLN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Serafin Orantes (PCN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()









        pregunta_est="¿Como evalúa usted el desempeño del actual alcalde ABILIO FLORES de Ahuachapán? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Malo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Regular"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Muy Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Excelente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Cree usted que el actual alcalde debe participar nuevamente como candidato a alcalde del municipio de Ahuachapán."
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Si"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="No"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

       
        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()






        pregunta_est="Si usted cree que el alcalde debe buscar la reelección, como le gustaría que lo hiciera. "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Que se reelija con su actual partido PCN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Que busque realizar una coalición o Alianza con otro partido"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="No me interesa, yo votare por otro candidato"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        
       
        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Supongamos que se reelige"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Como sea Yo voy a votar por el"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Yo votaría por el aunque se reelija con el PCN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Yo votaría Por el Si se reelige en Una coalición con otro Partido"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="Yo no votaría por el si se reelige con el PCN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()



        la_opcion="Independientemente lo que haga, yo no voy a votar por EL"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
       
        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        pregunta_est="Actualmente El Alcalde de Ahuachapan Pertenece al PCN ,Con que partido le recomendaría usted que haga una alianza o coalición"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="FMLN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="ARENA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="GANA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="NUEVAS IDEAS"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()



        la_opcion="CD"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
       
        la_opcion="PDC"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="OTRO"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No sabe/ No responde"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()



        pregunta_est="Es prematura la pregunta, pero queremos saber la fuerza de los partidos, Para Diputado que partido cree que debe tener mas diputados"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="FMLN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="ARENA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="GANA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="PCN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="NUEVAS IDEAS"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()



        la_opcion="CD"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
       
        la_opcion="PDC"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="OTRO"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No sabe/ No responde"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        pregunta_est="Suponga que es su candidato y que en su partido, Por cuall partido votaria usted para la Alcaldia de ahuachapán"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="FMLN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="ARENA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="GANA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="PCN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="NUEVAS IDEAS"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()



        la_opcion="CD"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
       
        la_opcion="PDC"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="OTRO"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No sabe/ No responde"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        connection.close()
        return render(request,'principal.html',locals())



def crear_estudio_CV(request):        
     
    
              
        import random
        import datetime  
        
# CATEGORIA_ESTUDIO=(
#             ('POLITICO', 'POLITICO'),           
#             ('ECONOMICA', 'ECONOMICA'),
#             ('PHICOSOCIAL', 'PHICOSOCIAL'),
#             ('COMERCIAL', 'COMERCIAL'),
#             ('ACADEMICO', 'ACADEMICO'),
#             ('CIENTIFICA', 'CIENTIFICA'),
#             ('DEPORTIVA', 'DEPORTIVA'),
#             ('SOCIAL', 'SOCIAL'),
#             ('TECNOLOGICO', 'TECNOLOGICO'),
#             )

# TIPO_ESTUDIO=(
#             ('PUBLICO', 'PUBLICO'),         
#             ('DE_PAGO', 'DE_PAGO'),
#             ('PRIVADO', 'PRIVADO'),                         
#             )

# CONFIANZA_NIVEL=(
#             ('75%', '75%'),         
#             ('80%', '80%'),
#             ('85%', '85%'), 
#             ('90%', '90%'),         
#             ('95%', '95%'),
#             ('95.5%', '95.5%'),
#             ('99%', '99%'),                         
#             )
        tipo_estudio="GRATIS"

        nombre_estudio="Estudio Sobre Corona Virus COVID 19 En el Salvador"
        date=datetime.datetime.now()
        precio=0.15
        precio_suscrip=10.00
        precio_est=200


        descripcion_del_estudio= "Estudio sobre el conocimiento de la poblacion sobre el corona Virus, Su impacto Social y Economico"
        recomendacion_estudio= "Realizar el estudio, entre su comunidad, "
        p1=Estudios(precio_del_estudio=precio_est,precio_por_suscripcion=precio_suscrip,costo_por_muestra=precio,nombre=nombre_estudio,descripcion=descripcion_del_estudio, recomendacion=recomendacion_estudio,fecha_inicio=date,fecha_final=date,fecha_ultima_actualizacion=date,tipo_de_estudio="DE_PAGO",n_muestras=200,universo=5000,error="1",confianza='95%')
        p1.save() 


            

        pregunta_est="Cual es su Sexo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Masculino"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Femenino "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Rango de edad "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="15 a 21 años (Joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="22 a 28 años (Adulto joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="29 a 40 años (Adulto)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="41 a 60 años (Adulto mayor)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="60  a 100 años (Tercera edad)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Nivel Academico "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Nunca he estudiado"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
                    
        la_opcion="Estudios Basicos"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Estudio hasta bachillerato o esta en bachillerato"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Tienen estudios tecnicos"
        p32=Opciones(pregunta=p21,opcion=la_opcion)

        la_opcion="Tienen un titulo Universitario o estudio en la Universidad"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
       


        pregunta_est="Que tan informado se siente sobre como evitar la enfermedad producida por el Virus COVID-19 "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Muy Informado"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Algo Informado"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Poco Informado"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Nada Informado"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Como califica la informacion brindada por el gobierno "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Muy Suficiente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Suficiente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Insuficiente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Muy insuficiente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Que sensacion le produce el Corona Virus"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="preocupacion"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Insertidumbre"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Es irrelevante"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Cual Cree que es la causa del corona Virus"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Tienen que ver con la accion del Ser Humano sobre el medio Ambiente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Tienen que ver con ell conflicto economico entre las grandes potencis"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Tienen que ver con la Naturaleza, la biologia y esas cosas, es algo natural"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Es una accion divina, es una prueba, pronto pasara."
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="esta tomando usted, precauciones contra el Corona Virus"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Si, todas"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Si Algunas"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Teniendo en cuenta la situacion de El Salvador, Como afectara a la pandemia"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Empeorara la situacion economica"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Puede abrir nuevas oportunidades"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No afectara"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        pregunta_est="Cuanto temor le genera la llegada de el corona virus a El Salvador"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Mucho"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Bastante"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Poco"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Nada"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Ha salido ultimamente de su casa?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Si, ha hacer unas cosas "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Si, obligadamente, muy pocas veces"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No, no he salido, execpto a emergencia"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No, no he salido"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        return render(request,'principal.html',locals())


def crear_estudio_PDAD(request):    
              
        import random
        import datetime  
        
# CATEGORIA_ESTUDIO=(
#             ('POLITICO', 'POLITICO'),           
#             ('ECONOMICA', 'ECONOMICA'),
#             ('PHICOSOCIAL', 'PHICOSOCIAL'),
#             ('COMERCIAL', 'COMERCIAL'),
#             ('ACADEMICO', 'ACADEMICO'),
#             ('CIENTIFICA', 'CIENTIFICA'),
#             ('DEPORTIVA', 'DEPORTIVA'),
#             ('SOCIAL', 'SOCIAL'),
#             ('TECNOLOGICO', 'TECNOLOGICO'),
#             )

# TIPO_ESTUDIO=(
#             ('PUBLICO', 'PUBLICO'),         
#             ('DE_PAGO', 'DE_PAGO'),
#             ('PRIVADO', 'PRIVADO'),                         
#             )

# CONFIANZA_NIVEL=(
#             ('75%', '75%'),         
#             ('80%', '80%'),
#             ('85%', '85%'), 
#             ('90%', '90%'),         
#             ('95%', '95%'),
#             ('95.5%', '95.5%'),
#             ('99%', '99%'),                         
#             )
        tipo_estudio="DE_PAGO"

        nombre_estudio="Registro (Mensual)  del indice de popularidad de Diputados del departamento de Ahuachapán)"
        date=datetime.datetime.now()
        precio=0.15
        precio_suscrip=10.00
        precio_est=800


        descripcion_del_estudio= "Con este estudio se puede monitorear el nivel de aceptacion que tienen los DIPUTADOS de Ahuachapan, de donde vienen y hacia donde van, en cuanto al nivel de popularidad "
        recomendacion_estudio= "Se recomienda hacer el estudio a personas mayores de edad, tratar de cumplir la cantidad de encuestas solicitadas y distribuirlas en el tiempo, es decir no las haga todas de un solo, la actualizacion se realizara cada 15 dias apartir de la fecha de inicio"
        p1=Estudios(precio_del_estudio=precio_est,precio_por_suscripcion=precio_suscrip,costo_por_muestra=precio,nombre=nombre_estudio,descripcion=descripcion_del_estudio, recomendacion=recomendacion_estudio,fecha_inicio=date,fecha_final=date,fecha_ultima_actualizacion=date,tipo_de_estudio="DE_PAGO",n_muestras=200,universo=5000,error="1",confianza='95%')
        p1.save() 


     

        pregunta_est="Seleccione el Municipio"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="AHUACHAPAN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        
        la_opcion="ATIQUIZAYA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN FRANCISCO MENENDEZ"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN PEDRO PUXTLA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="ATACO"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="APANECA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="TURIN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="EL REFUGIO"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="TACUBA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="GUAYMANGO"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="JUJUTLA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN LORENZO"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
      

        pregunta_est="Cual es su Sexo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Masculino"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Femenino "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Rango de edad "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="15 a 21 años (Joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="22 a 28 años (Adulto joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="29 a 40 años (Adulto)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="41 a 60 años (Adulto mayor)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="60  a 100 años (Tercera edad)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Relación Laboral"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Soy o estoy desempleado"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
                    
        la_opcion="Soy empleado Publico"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Soy empleado privado"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Soy empresario independiente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)

        la_opcion="N/S N/R"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()



        pregunta_est="Nivel Academico "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Nunca he estudiado"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
                    
        la_opcion="Estudios Basicos"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Estudio hasta bachillerato o esta en bachillerato"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Tienen estudios tecnicos"
        p32=Opciones(pregunta=p21,opcion=la_opcion)

        la_opcion="Tienen un titulo Universitario o estudio en la Universidad"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        



        pregunta_est="Como evalua usted el desempeño de el Diputado Arturo Magaña "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Malo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Regular"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Muy Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Excelente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        pregunta_est="Como evalua usted el desempeño de el Diputado Serafin Orantes "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Malo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Regular"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Muy Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Excelente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        pregunta_est="Como evalua usted el desempeño de la Diputada Guisela de Portillo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Malo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Regular"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Muy Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Excelente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()



        pregunta_est="Como evalua usted el desempeño de el Diputado Ricardo Godoy "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Malo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Regular"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Muy Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Excelente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Quien de estos diputados realiza mejor su trabajo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        
        
        la_opcion="Arturo Magaña (ARENA)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Ricardo Godoy (ARENA)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
        la_opcion="Isela de Portillo (FMLN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Serafin Orantes (PCN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Quien de estos diputados realiza Peor su trabajo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
        
        
        la_opcion="Arturo Magaña (ARENA)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Ricardo Godoy (ARENA)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
        la_opcion="Isela de Portillo (FMLN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Serafin Orantes (PCN)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        return render(request,'principal.html',locals())




def crear_estudio_PADA(request):        
     
    
              
        import random
        import datetime  
        
# CATEGORIA_ESTUDIO=(
#             ('POLITICO', 'POLITICO'),           
#             ('ECONOMICA', 'ECONOMICA'),
#             ('PHICOSOCIAL', 'PHICOSOCIAL'),
#             ('COMERCIAL', 'COMERCIAL'),
#             ('ACADEMICO', 'ACADEMICO'),
#             ('CIENTIFICA', 'CIENTIFICA'),
#             ('DEPORTIVA', 'DEPORTIVA'),
#             ('SOCIAL', 'SOCIAL'),
#             ('TECNOLOGICO', 'TECNOLOGICO'),
#             )

# TIPO_ESTUDIO=(
#             ('PUBLICO', 'PUBLICO'),         
#             ('DE_PAGO', 'DE_PAGO'),
#             ('PRIVADO', 'PRIVADO'),                         
#             )

# CONFIANZA_NIVEL=(
#             ('75%', '75%'),         
#             ('80%', '80%'),
#             ('85%', '85%'), 
#             ('90%', '90%'),         
#             ('95%', '95%'),
#             ('95.5%', '95.5%'),
#             ('99%', '99%'),                         
#             )
        tipo_estudio="DE_PAGO"

        nombre_estudio="Encuesta Que mide el nivel de popularidad de los alcaldes del Departamento de Ahuachapan)"
        date=datetime.datetime.now()
        precio=0.15
        precio_suscrip=10.00
        precio_est=800


        descripcion_del_estudio= "Con este estudio se puede monitorear el nivel de aceptacion que tienen las figuras publicas estudiadas, de donde vienen y hacia donde van, en cuanto al nivel de popularidad "
        recomendacion_estudio= "Se recomienda hacer el estudio a personas mayores de edad, tratar de cumplir la cantidad de encuestas solicitadas y distribuirlas en el tiempo, es decir no las haga todas de un solo, la actualizacion se realizara cada 15 dias apartir de la fecha de inicio"
        p1=Estudios(precio_del_estudio=precio_est,precio_por_suscripcion=precio_suscrip,costo_por_muestra=precio,nombre=nombre_estudio,descripcion=descripcion_del_estudio, recomendacion=recomendacion_estudio,fecha_inicio=date,fecha_final=date,fecha_ultima_actualizacion=date,tipo_de_estudio="DE_PAGO",n_muestras=200,universo=5000,error="1",confianza='95%')
        p1.save() 


     

        pregunta_est="Seleccione el Municipio/ Alcalde"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="AHUACHAPAN / Abilio Flores"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        
        la_opcion="ATIQUIZAYA / Ana Luisa Rodríguez de González "          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN FRANCISCO MENENDEZ / Adin Zetino"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN PEDRO PUXTLA / Carlos Armando Cabrera "          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="ATACO / Óscar Oliverio Gómez"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="APANECA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="TURIN / Hilda María de Quezada"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="EL REFUGIO / Wilfredo Barrientos"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="TACUBA /  Luis Carlos Milla"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="GUAYMANGO / José Ángel Figueroa"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="JUJUTLA / Víctor Manuel Martínez "          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN LORENZO / Álvaro Castillo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
      




        pregunta_est="Cual es su Sexo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Masculino"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Femenino "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Rango de edad "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="18 a 25 años (joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="26 a 35 años (Adulto)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="36 a 60 años (Adulto mayor)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="60  a 100 años (Tercera edad)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        



      

        pregunta_est="Como evalua usted el desempeño del Actual Alcalde de su municipio "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()

        la_opcion="Malo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Regular"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Muy Bueno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Excelente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        return render(request,'principal.html',locals())



def crear_estudio_APPS(request):        
     
    
              
        import random
        import datetime  
        
# CATEGORIA_ESTUDIO=(
#             ('POLITICO', 'POLITICO'),           
#             ('ECONOMICA', 'ECONOMICA'),
#             ('PHICOSOCIAL', 'PHICOSOCIAL'),
#             ('COMERCIAL', 'COMERCIAL'),
#             ('ACADEMICO', 'ACADEMICO'),
#             ('CIENTIFICA', 'CIENTIFICA'),
#             ('DEPORTIVA', 'DEPORTIVA'),
#             ('SOCIAL', 'SOCIAL'),
#             ('TECNOLOGICO', 'TECNOLOGICO'),
#             )

# TIPO_ESTUDIO=(
#             ('PUBLICO', 'PUBLICO'),         
#             ('DE_PAGO', 'DE_PAGO'),
#             ('PRIVADO', 'PRIVADO'),                         
#             )

# CONFIANZA_NIVEL=(
#             ('75%', '75%'),         
#             ('80%', '80%'),
#             ('85%', '85%'), 
#             ('90%', '90%'),         
#             ('95%', '95%'),
#             ('95.5%', '95.5%'),
#             ('99%', '99%'),                         
#             )
        tipo_estudio="DE_PAGO"

        nombre_estudio="Investigacion sobre Apps y/o proyectos de ventas Online y Servicio delibery En el Salvador"
        date=datetime.datetime.now()
        precio=0.15
        precio_suscrip=10.00
        precio_est=400


        descripcion_del_estudio= "Este estudio tiene como objetivo medir el conocimiento y nivel de aceptaccion que tienenn las APPS de ventas en linea y el servicio delibery que prestan, Se realizara el estudio a nivel de Todo el El Salvador"
        recomendacion_estudio= "Se recomienda realizar el estudio a personas mayores de edad, tengan acseso a internet y que normalmente utilizen equipo tecnologico de comunicacion movil, que tenga la capacidad de realizar compras en linea"
        p1=Estudios(precio_del_estudio=precio_est,precio_por_suscripcion=precio_suscrip,costo_por_muestra=precio,nombre=nombre_estudio,descripcion=descripcion_del_estudio, recomendacion=recomendacion_estudio,fecha_inicio=date,fecha_final=date,fecha_ultima_actualizacion=date,tipo_de_estudio="DE_PAGO",n_muestras=600,universo=55000,error="1",confianza='95%')
        p1.save() 


     

        pregunta_est="Seleccione el departamento"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="AHUACHAPAN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        
        la_opcion="CABAÑAS"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="CUSCATLAN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="CHALATENANGO"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="LA LIBERTAD"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="LA PAZ"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="LA UNION"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="MORAZAN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SANTA ANA"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN MIGUEL"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SONSONATE"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN SALVADOR"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="SAN VICENTE"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="USULUTAN"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

       



        pregunta_est="Cual es su Sexo "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Masculino"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Femenino "
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()





        pregunta_est="Rango de edad "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="15 a 21 años (Joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="22 a 28 años (Adulto joven)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="29 a 40 años (Adulto)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="41 a 60 años (Adulto mayor)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="60  a 100 años (Tercera edad)"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        



        pregunta_est="Sabe usted si en su departamento hay alguna App para entrega de productos a Domicilio (Comida, Productos de canasta basica, muebles, electrodomesticos, etc)"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Si"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="No"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

      


        pregunta_est="¿ independiente si hay o no en su departamento, sabe que es lo que entregan a domicilio? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Solo alimentos , comidas y bebidas"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Alimentos y artículos de canasta basica"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="de todo, Alimentos, artículos de canasta basica, y electrodomésticos, ropa, etc"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

       
        la_opcion="Ns/Nr"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()    




        pregunta_est="¿Cómo se dio cuenta de la existenci de estas plataformas compras en línea y entregas a domicilio?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Un amigo la tiene instalada y la utiliza"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="He visto a unos repartidores, me imagino que eso es"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

               
        la_opcion="Escuche en la radio."
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Yo investigue si existían"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="En las redes sociales he visto los anuncios"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ns/Nr"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()




        pregunta_est="Actualmente hace uso usted de estas plataformas? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Si, muy seguido"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Eventualmente"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="A pesar de tener instalada una, No hago uso de ellas"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
        la_opcion="No hago uso de ellas, no tengo instalada ninguna"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        



        pregunta_est="Porque usted No utiliza una App para compras en linea"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Me da desconfianza y creo que no me van a cumplir con el pedido"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Vivo lejos y hasta aqui no vienen"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No se si confiar, no me inspiran confianza esas cosas"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Ellos le piden a uno pagar con tarjeta de credito, y yo no tengo y ademas no me gusta pagar asi"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        
        la_opcion="Yo si uso las App de compras en linea y servicio delibery"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()






        pregunta_est="Si usted hiciera uso de estas plataformas. cual cree usted que es la mejor forma de pagar? "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Anticipado por medio de una tarjeta de crédito o Debito"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Deposito o transferencia Bancario"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Contra entrega en efectivo."
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Siempre y cuando sea seguro, de cualquier forma"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()



        pregunta_est="Supongamos que, Usted es usuario de una App de compras en linea, Usted compra un mueble que vale $70.00 Nuevo enn una empresa seria que usted conoce, Como cree usted que debe hacerce el negocio"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Debe el cliente pagar por Anticipado"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="50Xciento anticipado y el otro 50Xciento a la contra entrega"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Pagar cuando le lleven el producto a su casa."          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()


        pregunta_est="La misma pregunta  solo que suponga que usted es el vendedor, usted vende un mueble que vale $70.00 Nuevo, Como cree usted que debe hacerce el negocio"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="Debe el cliente pagar por Anticipado"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="50Xciento anticipado y el otro 50Xciento a la contra entrega"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Pagar cuando le lleven el producto a su casa."          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()




        
        pregunta_est="¿Esta usted deacuerdo en pagar un costo por el servicio a Domicilio?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Si"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="No"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

       
        


        pregunta_est="Como le parece mejor, en cuanto a la forma de pago del servicio a domicilio "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Pagar de acuerdo a una tarifa fija establecida, (cerca, lejos, muy lejos)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Pagar dependiendo de la cantidad de producto solicitado (un porcentaje)"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Depende del tipo de producto, la distancia, el tipo de transporte, hay que hacer un calculo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

            
        


        pregunta_est="Normalmente como hace sus pedidos de comida a domicilio"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Utilizo Whats App"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Uso Redes sociales como Facebook , y mesenger"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Uso Redes sociales como Facebook , y luego llamo por telefono"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="Marco el numero de telefono de la tienda y pido"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()


        la_opcion="No hago compra de comida en linea"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
       
      



        pregunta_est="¿Cómo se encuentra de satisfecho con la rapidez de el servicio a Domicilio?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Nada satisfecho"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Poco satisfecho"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Satisfecho"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="Muy satisfecho"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()



        
        pregunta_est="Por favor valore la relación calidad-precio del servicio recibido"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Bueno"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Malo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()      

      

        pregunta_est="Tiene alguna sugerencia de mejora sobre el servicio de Comidas a Domicilio?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Mayor Rapidez"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Menor precio"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Compromiso de entregar lo pedido"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        



        pregunta_est="¿Recomendaría usted el servicio a domicilio?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Si lo recomiendo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="No lo recomiendo"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()


        pregunta_est="¿Actualmente es usted usuario/a del algún servicio de COMIDAS A DOMICILIO  "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Si"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="No"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

      


        pregunta_est="¿Desde hace cuánto tiempo hace uso del servicio de Comidas a Domicilio?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Desde hece mas de 3 años"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Desde hace más de 2 Años"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Desde hace más de 1 Años"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="Hace Unos 6 meses"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Hace Unos 3 meses"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()


        la_opcion="Hace un mes"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="En estos días"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()




        pregunta_est="¿Qué tan dispuesto estaría usted a realizar la compras de productos diversos (Ropa, electrodomesticos, muebles, etc ), no específicamente comida?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Nada dispuesto"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Poco dispuesto"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Dispuesto"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
        

        la_opcion="Muy Dispuesto"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()




        pregunta_est="¿Cuál sería el tiempo de entrega máximo que usted estará dispuesto a esperar?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
       
        la_opcion="menos de 1 hora"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="mas de 1 hora"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()
                
        la_opcion="Depende de lo que pida, Comida quiero que sea rapido, otras cosas puedo esperar mas"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()


        


        pregunta_est="¿Cuál seria el promedio de gasto máximo que estaría dispuesto a comprar con esta modalidad de servicio en línea?"
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Hasta $10"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Hasta $20"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()         
 
        la_opcion="mas de $20"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        


        connection.close()
        return render(request,'principal.html',locals())

def crear_estudio_NUEVO(request):
   pass
   pass
   return render(request,'principal.html',locals())




















