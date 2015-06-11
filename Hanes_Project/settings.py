"""
Django settings for Hanes_Project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j-#5bun&*mkaculfx1@bc_7h732@3z!_gjtoin_z-!m*hov0fp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hanes_project_app',
    'imagefit',
    'captcha',
    'south',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Hanes_Project.urls'

WSGI_APPLICATION = 'Hanes_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#Database settings
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': 'hanes_project_db',                      # Or path to database file if using sqlite3.
         # The following settings are not used with sqlite3:
         'USER': 'postgres',
         'PASSWORD': 'root',
         'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
         'PORT': '',                      # Set to empty string for default.
     }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\','/'),)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\','/')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

NOCAPTCHA = True
CAPTCHA_FLITE_PATH = os.environ.get('CAPTCHA_FLITE_PATH',None)
CAPTCHA_LENGTH = '3'
CAPTCHA_FONT_SIZE = 30


IMAGEFIT_ROOT = '/media/'
IMAGEFIT_CACHE_ENABLED = True
#
IMAGEFIT_CACHE_BACKEND_NAME = 'imagefit'


try:
    from local_settings import *
except ImportError as e:
    pass

