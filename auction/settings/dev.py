from .base import *

DEBUG = True

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
AUTH_USER_MODEL = 'users.CustomUser'

WSGI_APPLICATION = 'auction.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
