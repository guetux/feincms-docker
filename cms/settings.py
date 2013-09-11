import os
import sys

WEBAPP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_BASEDIR = os.path.abspath(os.path.join(WEBAPP_DIR, os.path.pardir))

DEBUG = any((cmd in sys.argv for cmd in ('runserver', 'shell'))) \
    or os.environ.get('DEBUG', 'False') == 'True'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost',]

ADMINS = (
    ('FEINHEIT Developers', 'dev@feinheit.ch'),
)

MANAGERS = ADMINS

SECRET_KEY = os.environ.get('SECRET_KEY', '^opn24nsp2d#xo*8fsekuu910*$9hkq_d5o!g^+qmhhbp#c0-v')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(APP_BASEDIR, 'dev.db')
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TIME_ZONE = 'Europe/Zurich'

_ = lambda s: s

LANGUAGE_CODE = 'de'

LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
    ('fr', _('French')),
    ('it', _('Italian')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.join(APP_BASEDIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(WEBAPP_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(APP_BASEDIR, 'media')


ROOT_URLCONF = 'cms.urls'

if 'runserver' in sys.argv:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', '')
    EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', '')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True


DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'root@oekohosting.ch')
SERVER_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'root@oekohosting.ch')

TEMPLATE_DIRS = (
    os.path.join(WEBAPP_DIR, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'south',

    'mptt',
    'tinymce',
    'feincms',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'feincms_oembed',

    'cms',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

FEINCMS_RICHTEXT_INIT_CONTEXT = {
    'TINYMCE_JS_URL': '/static/tiny_mce/tiny_mce.js',
}

SOUTH_MIGRATION_MODULES = dict((app, 'cms.migrate.%s' % app) for app in (
    'medialibrary',
    'page',
    'elephantblog',
))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}