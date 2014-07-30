from .settings import *


# -----------------------------------------------------------------------------
# Settings for development
# -----------------------------------------------------------------------------

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# -----------------------------------------------------------------------------
# Debug Toolbar
# -----------------------------------------------------------------------------

INTERNAL_IPS = (
    '127.0.0.1',
    '84.127.246.117',
)


# -----------------------------------------------------------------------------
# Database (https://docs.djangoproject.com/en/1.6/ref/settings/#databases)
# -----------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# -----------------------------------------------------------------------------
# Email Configuration
# -----------------------------------------------------------------------------

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
DEFAULT_FROM_EMAIL = ''