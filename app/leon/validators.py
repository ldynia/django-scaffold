import os

from config.settings import BASE_DIR
from config.settings import INSTALLED_APPS
from leon.utilities import model_to_import_path


def valid_app_arg(**options):
    valid = True
    error = ''

    app = options.get('app')
    if not app or app == '':
        valid = False
        error = 'Missing app argument!'

    return valid, error

def valid_models_arg(**options):
    valid = True
    error = ''

    models = options.get('models')
    if not models or models == []:
        valid = False
        error = 'Missing models argument!'
    
    return valid, error

def app_exist(**options):
    valid = True
    error = ''

    app = options.get('app')
    normalized_apps = [app.split('.')[0] for app in INSTALLED_APPS]
    if app not in normalized_apps:
        valid = False
        error = f"Looks like application {app} is not installed!"
 
    return valid, error


def valid_model_path(**options):
    valid = True
    error = ''

    app = options.get('app')
    filename = options.get('model_filename')
    dir_path = options.get('model_dir_path')
    
    if dir_path:
        model_path = f'{dir_path}/{filename}'
    else:
        model_path = f'{BASE_DIR}/{app}/{filename}'
    
    if not os.path.exists(model_path):
        valid = False
        error = f"Model path {model_path} doesn't exist!"

    return valid, error


def valid_model(**options):
    valid = True
    error = ''

    app = options.get('app')
    models = options.get('models')
    filename = options.get('model_filename')
    dir_path = options.get('model_dir_path')
    
    if dir_path:
        model_path = f'{dir_path}/{filename}'
    else:
        model_path = f'{BASE_DIR}/{app}/{filename}'

    for model in models:
        model_import_path = model_to_import_path(model, model_path)
        try:
            exec(model_import_path)
        except ImportError:
            valid = False
            error = f'Cannot import {model} model path: {model_import_path}'

    return valid, error


def validate_options(**options):
    errors = []
    valid_opns = True

    valid, msg = valid_app_arg(**options)
    if not valid:
        valid_opns = False
        errors.append(msg)
    
    valid, msg = valid_models_arg(**options)
    if not valid:
        valid_opns = False
        errors.append(msg)
    
    valid, msg = app_exist(**options)
    if not valid:
        valid_opns = False
        errors.append(msg)

    valid, msg = valid_model_path(**options)
    if not valid:
        valid_opns = False
        errors.append(msg)
    
    valid, msg = valid_model(**options)
    if not valid:
        valid_opns = False
        errors.append(msg)

    return valid_opns, errors
