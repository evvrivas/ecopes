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



def logout(request):
    auth.logout(request)
    
    return HttpResponseRedirect("/")
       
#@login_required
def pagina_principal(request):   
                         
        return render(request,'principal.html',locals())  
                          
                
                       

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


def poner_lista_de_estudios(request):

        usuario_actual=request.user.username
        lista_de_codigos=Codigo.objects.filter(usuario__watsapp=usuario_actual)

        estudios_libres=Estudios.objects.filter(tipo_de_estudio="LIBRE")
        
        vector_de_estudios_de_pago=[]
        vector_de_estudios_privados=[]

        for i in lista_de_codigos:
              
              estudio=Estudios.objects.get(codigo=i.codigo,tipo_de_estudio="DE_PAGO")
             
              if estudio.tipo_de_estudio=="DE_PAGO":
                  vector_de_estudiosde_pago.append(estudio)
              else:
                  vector_de_estudios_privado.append(estudio)
             

        return render(request,'lista_de_estudios.html',locals())
     


def poner_cuestionario(request,id_estudio):

      vector_de_preguntas=[]
      
      estudio_actual=Estudios.objects.get(id=id_estudio)
      las_preguntas=Preguntas.objects.filter(estudio=estudio_actual)      
      
      for i in las_preguntas:
            
            las_opciones=Opciones.objects.filter(pregunta=i)

            vector_de_preguntas.append(las_opciones)
      

      
      connection.close()
      return render(request,'cuestionario.html',locals()) 



def crear_estudio(request):        
              
        import random
        import datetime  
        for i in range(10):

            a=random.randint(0,2)
            if a==0:
                tipo_estudio="LIBRE"

            elif a==1:
                tipo_estudio="DE_PAGO"

            elif a==1:
                tipo_estudio="PRIVADO"

            else:
                tipo_estudio="BUENO"

            nombre_estudio="ELECCION alcalde "+ str(i)
            codigo_del_estudio=str(i)
            date=datetime.datetime.now()

            p1=Estudios(nombre=nombre_estudio,descripcion="Este se realiza en ahuachapan municipio",descripcion_publica="ALCALDES DE AHUACHAPAN", fecha_inicio=date,fecha_final=date,codigo=codigo_del_estudio,tipo_de_estudio="LIBRE",n_muestras=100,universo=1000)
            p1.save() 

            for j in range(10):

                    pregunta_est="que es eso "+str(i) +str(j)
                    p21=Preguntas(estudio=p1, pregunta=pregunta_est)
                    p21.save()
                    
                    la_opcion="Opcion A "+str(i) +str(j)           
                    p31=Opciones(pregunta=p21,opcion=la_opcion)
                    p31.save()

                    la_opcion="Opcion B "+str(i) +str(j)
                    p32=Opciones(pregunta=p21,opcion=la_opcion)
                    p32.save()
                    
                    la_opcion="Opcion C "+str(i) +str(j)
                    p33=Opciones(pregunta=p21,opcion=la_opcion)
                    p33.save()
                    
                    la_opcion="Opcion D "+str(i) +str(j)
                    p34=Opciones(pregunta=p21,opcion=la_opcion)
                    p34.save()
                    
                    la_opcion="Opcion E "+str(i) +str(j)
                    p35=Opciones(pregunta=p21,opcion=la_opcion)
                    p35.save()

        connection.close()
        return render(request,'principal.html',locals()) 



     
     
def agregar_encuesta(request,id_estudio):
    
    if request.POST:
            id_estudio=id_estudio
            vector_de_preguntas=[]
            
            estudio_actual=Estudios.objects.get(id=id_estudio)
            las_preguntas=Preguntas.objects.filter(estudio=estudio_actual)      
            
            for i in las_preguntas:
                  
                  las_opciones=Opciones.objects.filter(pregunta=i)

                  vector_de_preguntas.append(las_opciones)
           
            seleccionadas=[]
                  
            for i in vector_de_preguntas:
              for k in i:
                 opcion_s = request.POST.get(k.pregunta.pregunta)
                 seleccionadas.append(opcion_s)
                 break

             
                #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
            connection.close()
            return render(request,'confirmar_encuesta.html',locals())             

    connection.close()
    return render(request,'principal.html',locals())        