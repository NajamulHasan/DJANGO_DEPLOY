import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTs=[os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS=['http://'+ os.environ['WEBSITE_HOSTNAME']]
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

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myapp', 'static'),
    # Add other paths to your static files if needed
]

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFileStorage'
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['AZURE_MYSQL_NAME'],
        'HOST': os.environ['AZURE_MYSQL_HOST'],
        'USER': os.environ['AZURE_MYSQL_USER'],
        'PASSWORD': os.environ['AZURE_MYSQL_PASSWORD'],
    }
}
