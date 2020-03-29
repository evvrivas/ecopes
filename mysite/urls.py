#from django.conf.urls import patterns, include, url
#from django.contrib import admin

#from mysite.views import Index

##########################
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url,include

from django.contrib import admin


from django.conf import settings
import mysite.settings

from django.contrib.auth.views import login, logout

from django.conf.urls.static  import static 


from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from mysite.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'artetronica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/',include(admin.site.urls)),
    #url(r'^$', Index.as_view(), name='index'),
    url(r'^accounts/login/$', login,{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', pagina_principal),    
    url(r'^$', pagina_principal),

    url(r'^crear_usuario/$',crear_usuario),
    url(r'^editar_usuario/$',editar_usuario),

    url(r'^poner_lista_de_estudios/([^/]+)/$',poner_lista_de_estudios),
    url(r'^poner_cuestionario/(\d+)/$',poner_cuestionario),
    url(r'^agregar_encuesta/(\d+)/$',agregar_encuesta),
    url(r'^habilitar_estudio/(\d+)/$',habilitar_estudio),

    url(r'^actualizar_previo_a_graficar/(\d+)/$',actualizar_previo_a_graficar),
    url(r'^informacion_del_estudio/(\d+)/$',informacion_del_estudio),    
    
    url(r'^pagina_de_analisis/(\d+)/(\d+)/([^/]+)/$',pagina_de_analisis),
    url(r'^hacer_grafico_de_barras/(\d+)/$',hacer_grafico_de_barras),
    url(r'^hacer_grafico_de_secuencia/(\d+)/$',hacer_grafico_de_secuencia),
    url(r'^hacer_grafico_de_tendencia/(\d+)/$',hacer_grafico_de_tendencia),
    url(r'^hacer_grafico_de_pastel/(\d+)/$',hacer_grafico_de_pastel),

    url(r'^graficar_cruse_de_datos/(\d+)/(\d+)/(\d+)/$',graficar_cruse_de_datos),
    
    url(r'^informacion/$',informacion),
    url(r'^busqueda/$', busqueda),
    url(r'^ver_mis_numeros/$',ver_mis_numeros),
    url(r'^manual_de_usuario/$',manual_de_usuario),
    
    url(r'^crear_estudio_CH5NOV/$',crear_estudio_CH5NOV),
    url(r'^crear_estudio_PDAD/$',crear_estudio_PDAD),
    url(r'^crear_estudio_PADA/$',crear_estudio_PADA),
    url(r'^crear_estudio_CV/$',crear_estudio_CV),
    url(r'^crear_estudio_FPMA/$',crear_estudio_FPMA),
    url(r'^crear_estudio_APPS/$',crear_estudio_APPS),
    url(r'^crear_estudio_NUEVO/$',crear_estudio_NUEVO),
    url(r'^crear_categorias/$',crear_categorias),
    
     

]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

