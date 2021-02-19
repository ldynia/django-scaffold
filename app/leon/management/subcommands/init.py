import json

from django.core.management.base import BaseCommand
from termcolor import cprint

from config.settings import BASE_DIR
from leon.validators import validate_options


class InitCommand(BaseCommand):

    help = "Create 'leon.json' from app and its model(s)."

    def add_arguments(self, parser):
        parser.add_argument('app', type=str, default=None, help='Application name.', nargs='?')
        parser.add_argument('models', type=str, default=None, help='Model name(s).', nargs='*')

        parser.add_argument('--api-type', type=str, default='graphql', help='Path to a file where model is defined.')
        parser.add_argument('--model-filename', type=str, default='models.py', help='Path to a file where model is defined.')
        parser.add_argument('--model-dir-path', type=str, default=None, help='Path to a file where model is defined.')


    def handle(self, *args, **options):
        # Validate cli args
        valid, errors = validate_options(**options)
        if not valid:
            for err in errors:
                cprint(err, 'yellow')
        else:
            self.create_json_init(**options)
            cprint(f"Created 'leon.json' file.", 'green')


    def create_json_init(self, **options):
        APP = options.get('app')
        MODEL = options.get('models')[0]
        API_TYPE = options.get('api_type')
        APP_OUTPUT_DIR = f"{BASE_DIR}/{APP}/api/{API_TYPE}/endpoints/{MODEL.lower()}"
        APP_BLUEPRINTS_DIR = f"{BASE_DIR}/{APP}/api/{API_TYPE}/blueprints/{MODEL.lower()}"
        MODEL_FILENAME = options.get('model_filename')
        MODEL_PATH = f'{BASE_DIR}/{APP}/{MODEL_FILENAME}'

        init_json = json.dumps({
            'apps': [
                {
                    'name': APP,
                    'models': [
                        {
                            'name': MODEL,
                            'path': MODEL_PATH,
                            'options': {
                                API_TYPE: {
                                    'output_dir': APP_OUTPUT_DIR,
                                    'blueprints_dir': APP_BLUEPRINTS_DIR,
                                }
                            },
                        }
                    ],
                }
            ],
        }, indent=2, sort_keys=True)

        with open(f'{BASE_DIR}/leon.json', 'w') as file:
            file.write(init_json)
