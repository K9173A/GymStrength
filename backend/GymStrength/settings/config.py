"""

"""
import os
import pathlib
import json

from django.core.exceptions import ImproperlyConfigured


def get_env_var(config_file_path, env_var_name):
    """
    Retrieves specific environment variable value from configuration file.
    :param config_file_path: json configuration file path.
    :param env_var_name: environment variable name.
    :return: environment variable value.
    """
    with open(config_file_path) as f:
        config_data = json.loads(f.read())
        env_var_value = config_data.get(env_var_name)
        if not env_var_value:
            raise ImproperlyConfigured(
                f'ImproperlyConfigured: set "{env_var_name}" environment variable'
            )
        return env_var_value


MODE = os.environ.get('GYMSTRENGTH_MODE')

if MODE == 'DEV':
    CONFIG_FILE = 'development.json'
elif MODE == 'PROD':
    CONFIG_FILE = 'production.json'
else:
    raise ValueError('Incorrect GYMSTRENGTH_MODE variable value')

CONFIG_DIR_PATH = os.path.join(pathlib.Path(__file__).parent, 'config')
CONFIG_BASE_FILE_PATH = os.path.join(CONFIG_DIR_PATH, 'base.json')
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR_PATH, CONFIG_FILE)

# Secret keys are stored in the config folder files
SECRET_KEY = get_env_var(CONFIG_BASE_FILE_PATH, 'SECRET_KEY')
# Allowed hosts
ALLOWED_HOSTS = get_env_var(CONFIG_BASE_FILE_PATH, 'ALLOWED_HOSTS')
# Root user name
DB_USER_NAME = get_env_var(CONFIG_BASE_FILE_PATH, 'DB_USER_NAME')
# Root user password
DB_USER_PASS = get_env_var(CONFIG_BASE_FILE_PATH, 'DB_USER_PASS')
# Mode
DEBUG = get_env_var(CONFIG_BASE_FILE_PATH, 'DEBUG')
