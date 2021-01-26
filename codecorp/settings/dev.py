from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '--d*hx&1k=2cro=o5#*bo#^n2tr&hxoc9kh1y64d2+7vc-=&w$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}