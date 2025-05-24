from .common import *

SECRET_KEY = 'django-insecure-qn%@y3!$1vpy6t^e+1_e&4i+v*14*idw7j2c((guthf!qq9=xd'

DEBUG = True

ALLOWED_HOSTS = []

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage'
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
