from settings import *


# -----------------------------------------------------------------------------
# Mounting a Django Application on a Subpath
# -----------------------------------------------------------------------------

# See http://docs.webfaction.com/software/django/config.html#mounting-a-django-application-on-a-subpath

# FORCE_SCRIPT_NAME = '/subdirectory'
# STATIC_URL = FORCE_SCRIPT_NAME + '/static/'
# MEDIA_URL = FORCE_SCRIPT_NAME + '/media/'


# -----------------------------------------------------------------------------
# Custom apps for staging
# -----------------------------------------------------------------------------

# INSTALLED_APPS += (
#     '',
# )


# -----------------------------------------------------------------------------
# Security
# -----------------------------------------------------------------------------

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS += ['#'] # Write here your project domain


# -----------------------------------------------------------------------------
# Database (https://docs.djangoproject.com/en/1.6/ref/settings/#databases)
# -----------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}