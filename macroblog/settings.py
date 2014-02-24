# Django absolute paths for settings.py

import os
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here('..')
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

# Django settings for macroblog project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG
PRODUCTION = True


ADMINS = (
    ('Mohammad Adil', 'mmadil_14@yahoo.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*',]

TIME_ZONE = 'Asia/Kolkata'

LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = root('media')
MEDIA_URL = ''

STATIC_ROOT = root('static')

STATICFILES_DIRS = (
        root('assets'),
)

TEMPLATE_DIRS = (
        root('templates'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'w5vxm3@i3x0i2&k87c!xjs8p$-%7(7g5ogh0yprk*uh-!58xgf'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'macroblog.urls'

WSGI_APPLICATION = 'macroblog.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    #'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
)

THIRD_PARTY_APPS = (
    'south',
)

LOCAL_APPS = (
    'blog',
    'widgets',
    'photoblog',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

import dj_database_url

DATABASES = {'default': dj_database_url.config()}

try:
    from local_settings import *
except ImportError:
    pass

if PRODUCTION:
    STATIC_URL = 'https://googledrive.com/host/0B-gIhJMz12BtMTFvY0lSSWF5S2s/'
else:
    STATIC_URL = '/static/'

