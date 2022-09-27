import os
from pathlib import Path

from decouple import config
from dj_database_url import parse as dburl

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

SECRET_KEY = 'django-insecure-%su4+wficji-5&i@4iob08cd1caq2!36*%!i59n-#i5g41u8os'

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'logbit-assessment.herokuapp.com',
    'simulador.logbit.com.br',
]

INSTALLED_APPS = [
    'avatar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_object_actions',
    'django_quill',
    'rest_framework',
    'django_filters',
    'nested_admin',
    'colorfield',
    'import_export',

    'assessment',
    'configuracao_assessment',
    'core',
    'curso',
    'dicas_oportunidades',
    'home',
    'kinetics',
    'perguntas',
    'respostas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'crum.CurrentRequestUserMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'home.middlewares.SidebarMiddleware',
]
# Para saber se redirecionamos para o auth ou não
if config('REDIRECT_KINETICS', default=False, cast=bool):
    MIDDLEWARE.append('kinetics.middlewares.RedirectMiddleware')

ROOT_URLCONF = 'logbit_assessment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'logbit_assessment.wsgi.application'

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

PRODUCAO = config('PRODUCAO', default=False, cast=bool)

if PRODUCAO:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DATABASE_POSTGRES'),
            'USER': config('USER_POSTGRES'),
            'PASSWORD':  config('PASSWORD_POSTGRES'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join('/var/www/html/static/')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join('/var/www/html/media/')
else:
    DATABASES = {
        'default': config(
            'DATABASE_URL',
            default=default_dburl,
            cast=dburl
        ),
    }
    
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

AVATAR_CACHE_ENABLED = False
AVATAR_THUMB_FORMAT = "PNG"
