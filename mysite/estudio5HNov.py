def crear_estudioCH5NOV(request):        
              
        import random
        import datetime  
        

        tipo_estudio="PUBLICO"

        nombre_estudio="Estudio de Disciplinas deportivas de interes en CH5NOV "+ str(i)
        codigo_del_estudio=0001
        date=datetime.datetime.now()

        descripcion_del_estudio= "Este se realiza entre trabajadores y beneficiarios de la Central Hidroelectrica 5 de Noviembre"

        p1=Estudios(nombre=nombre_estudio,descripcion=descripcion_del_estudio, fecha_inicio=date,fecha_final=date,codigo=codigo_del_estudio,tipo_de_estudio="PUBLICO",n_muestras=400,universo=400,error=0,confianza=0)
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



        pregunta_est="Le gustaria participar en estosotros deportes "
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

     

        pregunta_est="Asistiria usted a apoyar a los participantes "
        p21=Preguntas(estudio=p1, pregunta=pregunta_est)
        p21.save()
                    
        la_opcion="Si, Siempre voy"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()

        la_opcion="Si, cuando tengo tiempo y energias"          
        p31=Opciones(pregunta=p21,opcion=la_opcion)
        p31.save()


        la_opcion="No, prefiero descanzar"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="Hare el esfuerzo si hay insentivo (Vender comida), prefiero descanzar"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()

        la_opcion="No me gusta ir"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()


        la_opcion="Ns/Nr Ninguno"
        p32=Opciones(pregunta=p21,opcion=la_opcion)
        p32.save()








        connection.close()
        return render(request,'principal.html',locals())