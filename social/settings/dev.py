from .common import *

SECRET_KEY = 'django-insecure-qn%@y3!$1vpy6t^e+1_e&4i+v*14*idw7j2c((guthf!qq9=xd'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
