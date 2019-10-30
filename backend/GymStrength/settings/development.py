"""
This module implements settings used for development purposes.
Consider using it in your testing environment.
"""
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# ============================================================================
# Email
# ============================================================================
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_HOST_USER = 'admin@gymstrength.local'
EMAIL_HOST_PASSWORD = 'admin'
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/emails/'
