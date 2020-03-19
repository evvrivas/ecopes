def crear_estudio_POLITICA_AHUACHAPAN(request):        
              
        import random
        import datetime  
        

        tipo_estudio="PUBLICO"

        nombre_estudio="ENCUESTA OPINION PUBLICA, EVALUACION DE FIGURAS POLITICAS DE ACTUALIDAD "
        date=datetime.datetime.now()
        precio=0.15
        precio_suscrip=5.00
        precio_est=300


        descripcion_del_estudio= "Este estudio se realiza en el Municipio de Ahuachapán, con la intencion de obtener la persepcion que las personas tienen acerca del actuar tanto politico como personal de las personas que actualmente ostentan algun cargo de eleccion popular"
        recomendacion_estudio= "Se recomiendo buscar personas mayores de edad. que esten dispuestos a responder honestamente las preguntas"
        p1=Estudios(precio_del_estudio=precio_est,precio_por_suscripcion=precio_suscrip,costo_por_muestra=precio,nombre=nombre_estudio,descripcion=descripcion_del_estudio, recomendacion=recomendacion_estudio,fecha_inicio=date,fecha_final=date,fecha_ultima_actualizacion=date,tipo_de_estudio="PUBLICO",n_muestras=300,universo=400,error=1,confianza=97)
        p1.save() 


     

        pregunta_est="Cual es su relacionn con CH5NOV "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Soy Trabajador"          
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
