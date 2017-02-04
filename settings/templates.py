from settings.base import rel

CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # 'pangolinfog.context_processors.recaptcha',
)

TEMPLATES = [
    
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [rel('templates'),
                 rel('product/templates'),
                ],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': CONTEXT_PROCESSORS},
    }
]
