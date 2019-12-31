"""
This module implements settings used for development purposes.
Consider using it in your testing environment.
"""
from .config import get_env_var, CONFIG_FILE_PATH


DEBUG = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
EMAIL_HOST = get_env_var(CONFIG_FILE_PATH, 'SERVICE_ADDRESS')
EMAIL_PORT = '1025'
EMAIL_HOST_USER = f'admin@{get_env_var(CONFIG_FILE_PATH, "SERVICE_DOMAIN")}.com'
EMAIL_HOST_PASSWORD = 'admin'
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/emails/'
