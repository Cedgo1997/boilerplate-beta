from .base import *

DEBUG = False
ALLOWED_HOSTS = ['www.yourdomain.com']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.SISTEMADEGESTIONQUEUSES',
        'NAME': 'NOMBREDELSISTEMADEGESTION'
        'USER': 'YOURDBUSERNAME'
        'PASSWORD': 'YOURDBPASS'
        'HOST': 'LOCALHOST'
        'PORT': '' 
    }
}