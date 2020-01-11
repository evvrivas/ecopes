#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
def root(folder):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), '..',folder)



BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# openshift is our PAAS for now.
ON_PAAS = 'OPENSHIFT_REPO_DIR' in os.environ

if ON_PAAS:
    SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
else:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = ')_7av^!cy(wfx=k#3*7x+(=j^fzv+ot^1@sh9s9t=8$bu@r(z$'

# SECURITY WARNING: don't run with debug turned on in production!
# adjust to turn off when on Openshift, but allow an environment variable to override on PAAS
DEBUG = not ON_PAAS
DEBUG = DEBUG or os.getenv("debug","false").lower() == "true"
DEBUG = True

if ON_PAAS and DEBUG:
    print("*** Warning - Debug mode is on ***")

TEMPLATE_DEBUG = False

if ON_PAAS:
    ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS'], socket.gethostname()]
else:
    ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_mysql',
    'mysite',
    'mysite.datos_artetronica',
    'sorl.thumbnail',
    'dbbackup',  # django-dbbackup

)


DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': 'my/var/backups'}



MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

######################################################################
#import os
#import urlparse

DATABASES = {}
if 'OPENSHIFT_MYSQL_DB_URL' in os.environ:
    url = urlparse.urlparse(os.environ.get('OPENSHIFT_MYSQL_DB_URL'))

    DATABASES['default'] = {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
        }

elif 'OPENSHIFT_POSTGRESQL_DB_URL' in os.environ:
    url = urlparse.urlparse(os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL'))

    DATABASES['default'] = {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
        }

else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }

##############################################################



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#if ON_PAAS:
    # determine if we are on MySQL or POSTGRESQL
#    if "OPENSHIFT_POSTGRESQL_DB_USERNAME" in os.environ: 
    
#        DATABASES = {
#            'default': {
#                'ENGINE': 'django.db.backends.postgresql_psycopg2',  
#                'NAME':     os.environ['OPENSHIFT_APP_NAME'],
#                'USER':     os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
#                'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
#                'HOST':     os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
#                'PORT':     os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
#            }
#        }
#        
#    elif "OPENSHIFT_MYSQL_DB_USERNAME" in os.environ: 
#    
#        DATABASES = {
#            'default': {
#                'ENGINE': 'django.db.backends.mysql',
#                'NAME':     os.environ['OPENSHIFT_APP_NAME'],
#                'USER':     os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
#                'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
#                'HOST':     os.environ['OPENSHIFT_MYSQL_DB_HOST'],
#                'PORT':     os.environ['OPENSHIFT_MYSQL_DB_PORT'],
#            }
#        }

        
#else:
    # stock django, local development.
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.sqlite3',
#            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#        }
#    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



MEDIA_URL = '/media/'

if ON_PAAS:
    MEDIA_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media/')
else: 
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, JavaScript, Images)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
#MEDIA_URL = '/media/'

#####STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi','static')
STATIC_ROOT = root('staticstorage')# probando



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



STATICFILES_DIRS = (
    root('static'),
)
##STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
##    os.path.join(BASE_DIR,"static"),
##)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
 #   os.path.join(BASE_DIR, 'templates'),
#)


#AUTH_PROFILE_MODULE = "account.UserProfile"


#para utilizar y poder enviar por correo de gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'xgangasx@gmail.com'
EMAIL_HOST_PASSWORD = 'rootroot'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LOGIN_REDIRECT_URL = '/' #Or whatever you wish

