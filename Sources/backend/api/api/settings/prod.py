from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]



DATABASES = {    
   "default": {        
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "animal-chipization",
        "USER": "user",
        "PASSWORD": "password",
        "HOST": "database",
        "PORT": 5432,
    }
}
