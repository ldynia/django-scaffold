import os
  
from django.core.management.base import BaseCommand, CommandError
from jinja2 import Environment, FileSystemLoader

from config.settings import BASE_DIR
from leon.constants import SEQUENCE
from leon.utilities import animate

class Command(BaseCommand):
    animate(SEQUENCE)
    print("Ultimate GraphQL API bakery!\n")

    def add_arguments(self, parser):
        parser.add_argument('--app', type=str, help='Application name.')
        parser.add_argument('--config', type=str, default=f'{BASE_DIR}/leon.js', help='Path to leon.json config.')
        parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite existing scaffolds.')
        parser.add_argument('--template-dir', type=str, default=f'{BASE_DIR}/leon/templates', help='Path to tamplates directory.')
    
    def handle(self, *args, **options):
        print('options', options)
        pass
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
