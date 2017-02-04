ADMINS = (
    ('Admin', 'admin@pangolinfog.com'),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'robot@pangolinfog.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.pangolin.com'
EMAIL_HOST_USER = 'alexey@pangolin.com'
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = 587
