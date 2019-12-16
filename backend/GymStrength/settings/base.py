"""
This module defines basic settings used on both: development and production
configuration settings.
"""
import os
import json
import datetime
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

from .mode import MODE


def get_env_var(name):
    """
    Retrieves specific environment variable value from configuration file.
    :param name: environment variable name.
    :return: environment variable value.
    """
    config_dir_path = os.path.join(Path(__file__).parent, 'config')
    config_file_name = 'development.json' if MODE == 'DEV' else 'production.json'
    config_path = os.path.join(config_dir_path, config_file_name)
    with open(config_path) as f:
        config_data = json.loads(f.read())
        env_var_value = config_data.get(name)
        if not env_var_value:
            raise ImproperlyConfigured(
                f'ImproperlyConfigured: set "{name}" environment variable'
            )
        return env_var_value


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Secret keys are stored in the config folder files
SECRET_KEY = get_env_var('SECRET_KEY')
# Allowed hosts
ALLOWED_HOSTS = get_env_var('ALLOWED_HOSTS')
# Root user name
DB_USER_NAME = get_env_var('DB_USER_NAME')
# Root user password
DB_USER_PASS = get_env_var('DB_USER_PASS')
# Mode
DEBUG = get_env_var('DEBUG')

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
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
    'EMAIL': {'activation': 'api.authapp.views.ActivationEmailView'}
}

DJOSER_GYMSTRENGTH = {
    'protocol': 'http',
    'domain_address': 'localhost:8080',
    'domain_name': 'gymstrength.com',
}

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
