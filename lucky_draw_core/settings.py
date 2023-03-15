import os
import sys
from datetime import timedelta
from pathlib import Path

import environ
env = environ.Env(
    DEBUG=(bool, True)
)

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'user',
    'period',
    'lottery_bill',
    'prize',
    'candidate',
    'province',
    'district',
    'about',
    'slide',
    'footer',
    'village',
    'post',
    'prize_type',
    'period_type',


    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'sorl.thumbnail',
    'sorl_thumbnail_serializer',
    'django_cleanup.apps.CleanupConfig',
    'rest_framework_simplejwt.token_blacklist',



]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = 'lucky_draw_core.urls'

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

WSGI_APPLICATION = 'lucky_draw_core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USR'),
        'PASSWORD': os.getenv('DB_PWD'),
        'HOST': 'localhost',
        'POST': '5432'
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


LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",

]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'common.pagination.page.PageWithTotalPage',
    'PAGE_SIZE': 25,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'DOC_EXPANSION': 'none'
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


LANGUAGES = [
    ('la', ('Lao')),
    ('en', ('English')),
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'en', },
        {'code': 'la', },
    ),

    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,   # Default
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
THUMBNAIL_FORCE_OVERWRITE = True
# CANDIDATE_MODEL = 'candidate.models.Candidate'
# LOTTERY_BILL_MODEL = "lottery_bill.models.LotteryBill"
# PERIOD_MODEL = "period.models.Period"
# PRIZE_MODEL = "prize.models.Prize"
# PRIZE_DETAILS_MODEL = "prize_details.models.PrizeDetail"
