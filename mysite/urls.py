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

    url(r'^poner_lista_de_estudios/$',poner_lista_de_estudios),
    url(r'^poner_cuestionario/(\d+)$',poner_cuestionario),
    url(r'^agregar_encuesta/(\d+)$',agregar_encuesta),

    url(r'^crear_estudio/$',crear_estudio),    

]

    
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

