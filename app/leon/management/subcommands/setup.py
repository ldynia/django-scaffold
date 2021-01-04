import json

from django.core.management.base import BaseCommand
from termcolor import cprint

from config.settings import BASE_DIR
from leon.validators import validate_options


class SetupCommand(BaseCommand):
    
    help = "Create 'leon.json' from app and its model(s)."
    
    def add_arguments(self, parser):
        parser.add_argument('app', type=str, default=None, help='Application name.', nargs='?')
        parser.add_argument('models', type=str, default=None, help='Model name(s).', nargs='*')

        parser.add_argument('--model-filename', type=str, default='models.py', help='Path to a file where model is defined.')
        parser.add_argument('--model-dir-path', type=str, default=None, help='Path to a file where model is defined.')


    def handle(self, *args, **options):
        # Validate cli args
        valid, errors = validate_options(**options)
        if not valid:
            for err in errors:
                cprint(err, 'yellow')
        
        self.create_json_init(**options)
        
        cprint(f"Created 'leon.json' file.", 'green')


    def create_json_init(self, **options):
        init = json.dumps({
            'app': options.get('app'),
            'options': {},
            'model': options.get('models')[0]
        })

        with open(f'{BASE_DIR}/leon.json', 'w') as file:
            file.write(init)