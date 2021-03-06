import os
import json

try:
    with open ('/etc/secret.json') as config_file:
        conf = json.load(config_file)
except:
    with open ('./etc/secret.json') as config_file:
        conf = json.load(config_file)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = conf['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if conf.get('ENV') != 'D':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['www.rimmingtonspharmacy.net', 'rimmingtonspharmacy.net', '176.58.122.183', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',
    'contact',
    'about',
    'admin2',
    'rest_framework',
    'mailer',
    'django_crontab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pharmacy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

CRONJOBS = [
    ('* * * * *', 'booking.cron.cron_send')
]

WSGI_APPLICATION = 'pharmacy.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': conf['DB_NAME'],
        'HOST': conf['DB_HOST'],
        'PORT': conf['DB_PORT'],
        'USER': conf['DB_USER'],
        'PASSWORD': conf['DB_PASS'],
        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MAILER_EMAIL_THROTTLE = 100

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

MEDIA_ROOT = '/images/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

if conf.get('ENV') != 'D':
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = conf.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = conf.get('EMAIL_PASS')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "mailer.backend.DbBackend"
