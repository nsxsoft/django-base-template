# -*- coding: utf-8 -*-
"""
Django settings for discoveryapps project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import sys


# -----------------------------------------------------------------------------
# Project paths
# -----------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(BASE_DIR))
MEDIA_ROOT = os.path.realpath(os.path.join(SITE_ROOT, 'media'))
STATIC_ROOT = os.path.realpath(os.path.join(SITE_ROOT, 'static'))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# -----------------------------------------------------------------------------
# Security
# -----------------------------------------------------------------------------

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = '{{ secret_key }}'


# -----------------------------------------------------------------------------
# Application definition
# -----------------------------------------------------------------------------

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'south',
    'compressor',
)

LOCAL_APPS = (
    'utils',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# -----------------------------------------------------------------------------
# Middlewares
# -----------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# -----------------------------------------------------------------------------
# Internationalization (https://docs.djangoproject.com/en/1.6/topics/i18n/)
# -----------------------------------------------------------------------------

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# -----------------------------------------------------------------------------
# Template settings
# -----------------------------------------------------------------------------

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# -----------------------------------------------------------------------------
# Static & Media Urls (https://docs.djangoproject.com/en/1.6/howto/static-files/)
# -----------------------------------------------------------------------------

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
