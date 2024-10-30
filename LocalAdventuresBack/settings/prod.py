from .base import *
from corsheaders.defaults import default_headers

DEBUG = False
# CSRF configuracion.
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'https://local-advetures-tec.vercel.app',
]

# Configuración de ALLOWED_HOSTS
ALLOWED_HOSTS = [
    'localhost',  # Para permitir localhost
    'local-advetures-tec.vercel.app',  # Para permitir tu dominio en producción
    'someting-anzudes.pythonanywhere.com',  # Tu dominio en PythonAnywhere
]

#CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Para desarrollo local
    'https://local-advetures-tec.vercel.app',  # Para tu dominio en producción
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'x-csrftoken',
    'x-requested-with',
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
