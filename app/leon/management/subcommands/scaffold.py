import os
import json
from distutils.dir_util import copy_tree

from django.core.management.base import BaseCommand
from jinja2 import Environment, FileSystemLoader
from termcolor import cprint

from config.settings import BASE_DIR
from leon import LEON_EXTENSION
from leon.validators import validate_template


class ScaffoldCommand(BaseCommand):

    help = 'Bake templates.'

    def add_arguments(self, parser):
        parser.add_argument('json-file', type=str, default='leon.json', help='Leon json file.', nargs='?')

        parser.add_argument('--model-filename', type=str, default='models.py', help='Path to a file where model is defined.')
        parser.add_argument('--model-dir', type=str, default=None, help='Path to a file where model is defined.')

        parser.add_argument('--config', type=str, default=f'{BASE_DIR}/leon.js', help='Path to leon.json config.')
        parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite existing scaffolds.')

        parser.add_argument('--api-type', type=str, default='graphql', help='Path to a file where model is defined.')
        parser.add_argument('--template-name', type=str, default='test.leon', help='Path to tamplates directory.')
        parser.add_argument('--template-dir', type=str, default=f'{BASE_DIR}/leon/blueprints/demo', help='Path to tamplates directory.')
        parser.add_argument('--output-path', type=str, default='/tmp/test.py', help='Path to tamplates directory.')


    def handle(self, *args, **options):
        LEON_FILENAME = options.get('json-file')
        LEON_FILE_PATH = f"{BASE_DIR}/{LEON_FILENAME}"
        with open(LEON_FILE_PATH) as json_file:
            leon = json.load(json_file)

        self.create_dirs(leon)
        self.copy_blueprints(leon)
        self.bake_blueprints(leon)

        cprint(f'Baking done!', 'green')


    def create_dirs(self, options):
        for app in options['apps']:
            for model in app['models']:
                for api_type, settings in model['options'].items():
                    for setting, value in settings.items():
                        if setting.endswith('_dir'):
                            os.makedirs(value, exist_ok=True)


    def copy_blueprints(self, options):
        for app in options['apps']:
            for model in app['models']:
                for api_type, settings in model['options'].items():
                    SRC = f"{BASE_DIR}/leon/blueprints/{api_type}/"
                    for setting, value in settings.items():
                        if setting == 'input_blueprints_dir':
                            blueprints_dir = model['options'][api_type]['input_blueprints_dir']
                            copy_tree(SRC, blueprints_dir)


    def bake_blueprints(self, options):
        for app in options['apps']:
            for model in app['models']:
                for api_type, settings in model['options'].items():
                    if api_type == 'graphql':
                        TEMPLATE_INPUT_DIR = model['options'][api_type]['input_blueprints_dir']
                        TEMPLATE_OUTPUT_DIR = model['options'][api_type]['output_blueprints_dir']
                        templates = self.get_templates(TEMPLATE_INPUT_DIR)
                        for template in templates:
                            template_path = f'{TEMPLATE_INPUT_DIR}/{template}'
                            valid_input = validate_template(TEMPLATE_INPUT_DIR, template_path)
                            if valid_input:
                                baked_template = self.generate_template(TEMPLATE_INPUT_DIR, template, **model)
                                out_path = f"{TEMPLATE_OUTPUT_DIR}/{template.replace(LEON_EXTENSION, '.py')}"
                                self.write_template(out_path, baked_template)


    def get_templates(self, dir, extention='.leon'):
        for root, dirs, files in os.walk(dir):
            return [filename for filename in files if filename.endswith(extention)]


    def generate_template(self, template_dir, template_name, **data):
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)

        return template.render(data)


    def write_template(self, output_path, template):
        with open(output_path, "w") as file:
            file.write(template)
