"""
This module defines basic settings used on both: development and production
configuration settings.
"""
import os
import datetime

from .config import MODE


if MODE == 'DEV':
    from .development import *
elif MODE == 'PROD':
    from .production import *
else:
    raise ValueError('Incorrect GYMSTRENGTH_MODE variable value')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================================
# Application definition
# ============================================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'corsheaders',
    'api.authapp',
    'api.gymapp',
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

ROOT_URLCONF = 'GymStrength.urls'

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

WSGI_APPLICATION = 'GymStrength.wsgi.application'

# ============================================================================
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# ============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gymstrength',
        'USER': DB_USER_NAME,
        'PASSWORD': DB_USER_PASS,
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# ============================================================================
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# ============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================================================
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# ============================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ============================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# ============================================================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

# ============================================================================
# Authentication
# ============================================================================
AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend',)
)
AUTH_USER_MODEL = 'authapp.User'

# ============================================================================
# Django REST framework settings
# ============================================================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

# ============================================================================
# Djoser settings
# ============================================================================
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/users/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/users/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/users/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
    'EMAIL': {'activation': 'api.authapp.views.ActivationEmailView'}
}

# DJOSER_GYMSTRENGTH = {
#     'protocol': get_env_var('PROTOCOL'),
#     'domain_address': f'localhost:8080',
#     'domain_name': 'gymstrength.com',
# }

# ============================================================================
# djangorestframework_simplejwt settings
# ============================================================================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=30),
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ============================================================================
# django-cors-headers settings
# ============================================================================
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

# ============================================================================
# Other custom settings
# ============================================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
USER_AVATARS_DIR_NAME = 'user_avatars'
