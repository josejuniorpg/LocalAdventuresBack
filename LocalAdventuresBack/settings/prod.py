from .base import *

DEBUG = False

ALLOWED_HOSTS = ['someting-anzudes.pythonanywhere.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
