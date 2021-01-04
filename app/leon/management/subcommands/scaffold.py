from django.core.management.base import BaseCommand
from jinja2 import Environment, FileSystemLoader
from termcolor import cprint

from config.settings import BASE_DIR
from leon.validators import validate_options, validate_template


class ScaffoldCommand(BaseCommand):

    help = 'GraphQL API bakery.'

    def add_arguments(self, parser):
        parser.add_argument('app', type=str, default=None, help='Application name.', nargs='?')
        parser.add_argument('models', type=str, default=None, help='Model name(s).', nargs='*')
        
        parser.add_argument('--model-filename', type=str, default='models.py', help='Path to a file where model is defined.')
        parser.add_argument('--model-dir', type=str, default=None, help='Path to a file where model is defined.')
        
        parser.add_argument('--config', type=str, default=f'{BASE_DIR}/leon.js', help='Path to leon.json config.')
        parser.add_argument('--overwrite', type=bool, default=False, help='Overwrite existing scaffolds.')
        
        parser.add_argument('--template-name', type=str, default='test.leon', help='Path to tamplates directory.')
        parser.add_argument('--template-dir', type=str, default=f'{BASE_DIR}/leon/templates/demo', help='Path to tamplates directory.')
        parser.add_argument('--output-path', type=str, default='/tmp/test.py', help='Path to tamplates directory.')
    

    def handle(self, *args, **options):
        # Validate cli args
        valid, errors = validate_options(**options)
        if not valid:
            for err in errors:
                cprint(err, 'yellow')

        # Setup templates
        template_name = options.get('template_name')
        template_dir = options.get('template_dir')
        template_file = f'{template_dir}/{template_name}'
        
        output_path = options.get('output_path')
        valid_input = validate_template(output_path, template_file)
        if valid_input:
            data = {
                'app': options.get('app'),
                'model': options.get('models')[0]
            }
            templ_str = self.generate_template(template_dir, template_name, **data)
            
            self.write_template(output_path, templ_str)
        
        cprint(f'Baking done! Check {output_path}', 'green')

    
    def generate_template(self, template_dir, template_name, **data):
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)

        return template.render(data)

    
    def write_template(self, output_path, template_str):
        with open(output_path, "w") as file:
            file.write(template_str)
