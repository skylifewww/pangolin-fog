import sys
from pathlib import Path

BASE_DIR = Path()


def rel(*x):
    return str(BASE_DIR.joinpath(*x).absolute())

DEBUG = False
DOMAIN = 'localhost:8000'
SFDOMAIN = '136.144.130.186' 

APPEND_SLASH = True
ALLOWED_HOSTS = ["pangolinsmoke.herokuapp.com", "smokefactory.us", "smoke-factory.us", "hazemachines.us", DOMAIN, SFDOMAIN]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_AGE = 1209600  # (2 weeks)
SESSION_COOKIE_NAME = 'sessionid'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SECRET_KEY = '=q02ytwt#x3mlha%(fh59-3(t_1%9r=*+(yua+%!_57+gd2t*4'

NORECAPTCHA_SITE_KEY = '6Lc-6RMUAAAAAK6fpqzOzOX3rBOMi0WnxV4rB3kJ'
NORECAPTCHA_SECRET_KEY = '6Lc-6RMUAAAAAE82SzOKopia8mBP8trknVlI_T0s'

NOCAPTCHA = True

# RECAPTCHA_PROXY = 'http://127.0.0.1:8000'


ROOT_URLCONF = 'pangolinfog.urls'

WSGI_APPLICATION = 'wsgi.application'

TESTING = 'test' in sys.argv[0]
DEVELOPMENT = 'run.py' in sys.argv or 'runserver' in sys.argv or 'collectstatic' in sys.argv

if 'test' in sys.argv:
    print('\033[1;91mNo django tests.\033[0m')
    print('Try: \033[1;33mpy.test\033[0m')
    sys.exit(0)
