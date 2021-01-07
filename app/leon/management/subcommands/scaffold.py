import os
import json

from django.core.management.base import BaseCommand
from jinja2 import Environment, FileSystemLoader
from termcolor import cprint

from config.settings import BASE_DIR
from leon.validators import validate_options, validate_template


class ScaffoldCommand(BaseCommand):

    help = 'Code bakery.'

    def add_arguments(self, parser):
        parser.add_argument('json-file', type=str, default='leon.json', help='Leon json file.', nargs='?')
        
        parser.add_argument('--model-filename', type=str, default='models.py', help='Path to a file where model is defined.')
        parser.add_argument('--model-dir', type=str, default=None, help='Path to a file where model is defined.')
        
        parser.add_argument('--config', type=str, default=f'{BASE_DIR}/leon.js', help='Path to leon.json config.')
        parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite existing scaffolds.')
        
        parser.add_argument('--template-name', type=str, default='test.leon', help='Path to tamplates directory.')
        parser.add_argument('--template-dir', type=str, default=f'{BASE_DIR}/leon/blueprints/demo', help='Path to tamplates directory.')
        parser.add_argument('--output-path', type=str, default='/tmp/test.py', help='Path to tamplates directory.')
    

    def handle(self, *args, **options):
        LEON_FILENAME = options.get('json-file')
        LEON_FILE_PATH = f"{BASE_DIR}/{LEON_FILENAME}"
        with open(LEON_FILE_PATH) as json_file:
            leon = json.load(json_file)
        
        # Make dirs
        for app in leon['apps']:
            print('gg',app['options'])
            for option, val in app['options'].items():
                if option.endswith('_dir'):
                     os.makedirs(val, exist_ok=True)
            

        # # Setup templates
        # template_name = options.get('template_name')
        # template_dir = options.get('template_dir')
        # template_file = f'{template_dir}/{template_name}'
        
        # output_path = options.get('output_path')
        # valid_input = validate_template(output_path, template_file)
        # if valid_input:
        #     data = {
        #         'app': options.get('app'),
        #         'model': options.get('models')[0]
        #     }
        #     templ_str = self.generate_template(template_dir, template_name, **data)
            
        #     self.write_template(output_path, templ_str)
        
        cprint(f'Baking done!', 'green')

    
    def generate_template(self, template_dir, template_name, **data):
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)

        return template.render(data)

    
    def write_template(self, output_path, template_str):
        with open(output_path, "w") as file:
            file.write(template_str)
