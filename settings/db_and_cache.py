import os
import dj_database_url
from django.conf.global_settings import DATABASES

ATOMIC_REQUESTS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pangolinfog',
        'USER': 'skywww',
        'PASSWORD': 'skywww123',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/0',
#     },
#     'local': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'pangolinfog'
#     }
# }
