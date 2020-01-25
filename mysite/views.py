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

      vector_de_opciones=[]
      
      estudio_actual=Estudios.objects.get(id=id_estudio)
      las_preguntas=Preguntas.objects.filter(estudio=estudio_actual)      
      
      for i in las_preguntas:
            
            las_opciones=Opciones.objects.filter(pregunta=i)

            vector_de_opciones.append(las_opciones)
      

      
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

            p1=Cuestionario_temporal(estudio=estudio_actual,respuesta_1=respuesta_1,respuesta_2=respuesta_2,respuesta_3=respuesta_3,respuesta_4=respuesta_4,respuesta_5=respuesta_5,
                                      respuesta_6=respuesta_6,respuesta_7=respuesta_7,respuesta_8=respuesta_8,respuesta_9=respuesta_9,respuesta_10=respuesta_10,
                                      respuesta_11=respuesta_11,respuesta_12=respuesta_12,respuesta_13=respuesta_13,respuesta_14=respuesta_14,respuesta_15=respuesta_15,
                                      respuesta_16=respuesta_16,respuesta_17=respuesta_17,respuesta_18=respuesta_18,respuesta_19=respuesta_19,respuesta_20=respuesta_20,
                                      respuesta_21=respuesta_21,respuesta_22=respuesta_22,respuesta_23=respuesta_23,respuesta_24=respuesta_24,respuesta_25=respuesta_25,
                                      respuesta_26=respuesta_26,respuesta_27=respuesta_27,respuesta_28=respuesta_28,respuesta_29=respuesta_29,respuesta_30=respuesta_30,
                                      respuesta_31=respuesta_31,respuesta_32=respuesta_32,respuesta_33=respuesta_33,respuesta_34=respuesta_34,respuesta_35=respuesta_35,
                                      respuesta_36=respuesta_36,respuesta_37=respuesta_37,respuesta_38=respuesta_38,respuesta_39=respuesta_39,respuesta_40=respuesta_40,
                                      respuesta_41=respuesta_41,respuesta_42=respuesta_42,respuesta_43=respuesta_43,respuesta_44=respuesta_44,respuesta_45=respuesta_45,
                                      respuesta_46=respuesta_46,respuesta_47=respuesta_47,respuesta_48=respuesta_48,respuesta_49=respuesta_49,respuesta_50=respuesta_50) 
                #guarda la palabra buscada siempre y cuando no exista EN EL REGISTRO DE BUSQUEDA
            p1.save()

            tabla_datos=Cuestionario_temporal.objects.all()
            connection.close()
            return render(request,'confirmar_encuesta.html',locals())             

    connection.close()
    return render(request,'principal.html',locals())



def actualizar_previo_a_graficar(request,id_estudio):

      id_estudio=id_estudio
      estudio_actual=Estudios.objects.get(id=id_estudio)
      las_preguntas=Preguntas.objects.filter(estudio=estudio_actual)      


      datos_temporales=Cuestionario_temporal.objects.filter(estudio_id=id_estudio)
      
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


      Cuestionario_temporal.objects.filter(estudio_id=id_estudio).delete()
      
      return render(request,'confirmar_encuesta.html',locals())


def guardar_en_acumulados(vector_de_acumulados,pregunta_actual):
         
             #keys = list_freq.keys();
             #values = list_freq.values()
         
             #for key, value in list_freq.items():
                 #print(key, " has count ", value)
                 #vector_de_acumulados.append(value)

             va=vector_de_acumulados
             t=len(vector_de_acumulados)
             a=0
             if t==1:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0])
             elif t==2:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1])
             elif t==3:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2])
             elif t==4:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3])
             elif t==5:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4])
             elif t==6:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5])
             elif t==7:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6])
             elif t==8:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6],opcion_8=va[7])
             elif t==9:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6],opcion_8=va[7],opcion_9=va[8])
             elif t==10:
                 p=Opciones_acumuladas(pregunta=pregunta_actual,opcion_1=va[0],opcion_2=va[1],opcion_3=va[2],opcion_4=va[3],opcion_5=va[4],opcion_6=va[5],opcion_7=va[6],opcion_8=va[7],opcion_9=va[8],opcion_10=va[9])

             else:
                 a=1

             if a==0:
                  p.save() 



def pagina_de_analisis(request, id_pregunta,badera):
    pregunta=Preguntas.objects.get(id=id_pregunta)
    opci=Opciones.objects.filter(pregunta_id=id_pregunta) 
    nombre_de_pregunta=pregunta.pregunta   
    id_pregunta=id_pregunta
    badera=bandera
    return render(request,'pagina_de_analisis.html',locals())

def hacer_grafico_de_barras(request,id_pregunta):
        vector_de_opciones=[]
        vector_de_repeticiones=[]
        opci=Opciones.objects.filter(pregunta_id=id_pregunta)       
      

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
       
        #plt.gca().set_yscale('log')

       
        bar_width = 0.45
        plt.bar(X, Y1, bar_width, color='b')

               
      
        #z=0 
        #for x, y in zip(X, Y1):
        #    plt.text(x, y+1 ,str(y)+ "\n"+vector_de_opciones[z], ha='center', va= 'bottom')
        #    z=z+1
 
      
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




def hacer_grafico_de_pastel(request,id_pregunta):
        vector_de_opciones=[]
        vector_de_repeticiones=[]
        opci=Opciones.objects.filter(pregunta_id=id_pregunta)       
      

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


        desfase = (0.1, 0, 0, 0, 0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

        color=["red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray"] 
      
        
        plt.pie(X, labels=vector_de_opciones, autopct="%0.1f %%", colors=color, explode=desfase)
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
       
       opcion_secuencial=Opciones_acumuladas.objects.filter(pregunta_id=id_pregunta)
       texto=[field.name for field in Opciones_acumuladas._meta.get_fields()]

       nombre_opcion=Opciones.objects.filter(pregunta_id=id_pregunta)
       
       vector_de_secuencias=[]

       x=len(nombre_opcion)+2
       for i in range(2,x):
            vector1=opcion_secuencial.values_list(texto[i], flat=True)
            vector2=np.asarray(vector1)
            vector3=[]

            for j in range(len(vector2)):
                if j ==0:
                    vector3.append(vector2[j])
                
                else:
                    b=j-1
                    c=vector2[j]+vector3[b]
                    vector3.append(c)
                

                total=sum(vector3)
                vector33=vector3*100/total

            vector_de_secuencias.append(vector33)
        
       X= np.arange(len(vector2))
       print(vector_de_secuencias)
       #barh(pos,datos,align = 'center')
       f=plt.figure()
       color=["red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow"] 
       b=0
       for i in vector_de_secuencias:
                plt.plot(X,i, color[b],"o-")
                b=b+1
               

       plt.grid()     
        

       leyenda="Variacion de la respuesta"
       plt.xlabel(leyenda)
           
       plt.ylabel('PREFERENCIAS')
       titulo="Variacion del las preferencias"
       plt.xticks(())
       plt.yticks(())
      
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
       
       opcion_secuencial=Opciones_acumuladas.objects.filter(pregunta_id=id_pregunta)
       texto=[field.name for field in Opciones_acumuladas._meta.get_fields()]

       nombre_opcion=Opciones.objects.filter(pregunta_id=id_pregunta)
       
       vector_de_secuencias=[]

       x=len(nombre_opcion)+2
       for i in range(2,x):
            vector1=opcion_secuencial.values_list(texto[i], flat=True)
            vector2=np.asarray(vector1)
            vector3=vector2
            total=sum(vector2)
            vector3=vector2*100/total
            #for j in range(len(vector2)):
                #if j ==0:
                    #vector3.append(vector2[j])
                
                #else:
                    #b=j-1
                    #c=vector2[j]+vector3[b]
                    #vector3.append(c)
            vector_de_secuencias.append(vector3)
        
       X= np.arange(len(vector2))
       print(vector_de_secuencias)
       #barh(pos,datos,align = 'center')
       f=plt.figure()
       color=["red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow","red","black","blue","green","orange","gray","yelow"] 
       b=0
       for i in vector_de_secuencias:
                plt.plot(X,i, color[b],"o-")
                b=b+1
               

       plt.grid()     
        

       leyenda="Variacion de la respuesta"
       plt.xlabel(leyenda)
           
       plt.ylabel('PREFERENCIAS')
       titulo="Variacion del las preferencias"
       plt.xticks(())
       plt.yticks(())
      
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


