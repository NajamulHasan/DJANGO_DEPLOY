import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]  # Fixed typo in ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS = ['http://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Corrected the path
]


STATIC_URL='/static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFileStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['AZURE_MYSQL_NAME'],
        'HOST': os.environ['AZURE_MYSQL_HOST'],
        'USER': os.environ['AZURE_MYSQL_USER'],
        'PASSWORD': os.environ['AZURE_MYSQL_PASSWORD'],
    }
}
