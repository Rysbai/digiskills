import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config, Csv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
DEBUG = (config('DEBUG') == 'True')

ALLOWED_HOSTS = ['64.225.36.157', '127.0.0.1', 'digiskills.kg', 'www.digiskills.kg']
HOST_NAME = config('HOST_NAME')
PORT = config('PORT')
SSL_SECURED = (config('SSL_SECURED') == 'True')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'django_summernote',
    'django_extensions',
    'django_cleanup.apps.CleanupConfig',

    'course.apps.CourseConfig',
    'news.apps.NewsConfig',
    'contacts.apps.ContactsConfig',
    'aboutus.apps.AboutusConfig',
    'comment.apps.CommentConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digiskills.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'digiskills.wsgi.application'

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': '',
        }
    }

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/back_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'back_static/')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('SMTP_HOST')
EMAIL_PORT = config('SMTP_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('SMTP_LOGIN')
EMAIL_HOST_PASSWORD = config('SMTP_PASSWORD')

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


sentry_sdk.init(
    dsn="https://393f4aea48b94ed680d0e0eb0c600fbb@sentry.io/1857344",
    integrations=[DjangoIntegration()]
)
