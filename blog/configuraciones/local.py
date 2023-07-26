#se importa todas las configuraciones del settings.py al local.py
from .settings import *




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER':'root',
        'PASSWORD':'723235vid',
        'HOST':'localhost',
        'PORT': 3306,
    }
}

