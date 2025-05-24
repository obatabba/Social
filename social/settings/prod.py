import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

CSRF_TRUSTED_ORIGINS = CSRF_ALLOWED_ORIGINS = CORS_ORIGINS_WHITELIST = [os.environ['HOST_URL']]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MEDIA_URL = '/media/'

DATABASES = {
    'default': dj_database_url.parse(
        os.environ['DATABASE_URL'],
        conn_max_age=600,
        conn_health_checks=True,
    )
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# CLOUDINARY_STORAGE = {        # Either use these OR the CLOUDINARY_URL environment variable
#     'CLOUD_NAME': 'your-cloud-name',
#     'API_KEY': 'your-api-key',
#     'API_SECRET': 'your-secret-key',
# }
