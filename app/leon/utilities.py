import re
import os
import time

from leon.constants import ASCII_ART


def animate(sequence, delay=0.4):
    os.system('clear')
    for frame in sequence:
        print(f"\r{frame}", flush=True)
        time.sleep(delay)
        os.system('clear')
    print(ASCII_ART)


def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


def model_to_import_path(model, path):
    module_path = path.replace('/app', '').replace('py', '').replace('/', '.').strip('.')
    return f'from {module_path} import {model}'
