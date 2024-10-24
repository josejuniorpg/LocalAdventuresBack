# Local imports
from .base import *

DEBUG = True

# Applications from base + local
INSTALLED_APPS += []

CORS_ALLOWED_ORIGINS = ['https://local-advetures-tec.vercel.app', 'http://localhost:3000']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# LINK_BASE_URL = 'http://127.0.0.1:8000/'
