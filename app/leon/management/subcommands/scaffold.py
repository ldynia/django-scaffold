import os
  
from django.core.management.base import BaseCommand, CommandError
from jinja2 import Environment, FileSystemLoader
from termcolor import colored, cprint

from config.settings import BASE_DIR
from leon.validators import (valid_arg, app_exist)


def validate_args(**options):
    app = options.get('app')
    if not valid_arg(app):
        return False, 'Missing required argument app.'
        
    if not app_exist(app):
        return False, f'Application "{app}" is not installed. '


class ScaffoldCommand(BaseCommand):
    help = 'GraphQL API bakery.'

    def add_arguments(self, parser):
        parser.add_argument('app', type=str, default=None, help='Application name.', nargs='?')
        parser.add_argument('--config', type=str, default=f'{BASE_DIR}/leon.js', help='Path to leon.json config.')
        parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite existing scaffolds.')
        parser.add_argument('--template-dir', type=str, default=f'{BASE_DIR}/leon/templates', help='Path to tamplates directory.')
    
    def handle(self, *args, **options):
        valid, error = validate_args(**options)
        if not valid:
            cprint(error, 'yellow')
        
        # template_name = options.get('template_name')
        # template_file = f"{template_dir}/{template_name}"

        # valid_input = self.validate(output_path, template_file)
        # if valid_input:
        #     data = {
        #         'app': options.get('app')[0],
        #         'model': options.get('model')[0]
        #     }
        #     templ_str = self.generate_template(template_dir, template_name, **data)
            
        #     self.write_template(output_path, templ_str)
        
        # print(self.style.SUCCESS('Baking done'))

    def generate_template(self, template_dir, template_name, **data):
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)

        return template.render(data)

    def validate(self, output_path, template_file):
        try:
            output_dir = '/'.join(output_path.split('/')[:-1])
            assert os.path.exists(output_dir), f"Dir {output_dir} doesn't exist!"
            assert os.access(output_dir, os.W_OK), f"Dir {output_dir} isn't writable!"
            assert os.path.isfile(template_file), f"File {template_file} isn't a file!"
            return True
        except AssertionError as err:
            print(self.style.ERROR(err))
            return False
    
    def write_template(self, output_path, template_str):
        with open(output_path, "w") as file:
            file.write(template_str)
