import os


MODE = os.environ.get('GYMSTRENGTH_MODE')
if MODE not in ['DEV', 'PROD']:
    raise ValueError('Incorrect GYMSTRENGTH_MODE variable value')
