import os

from django.core.management.base import BaseCommand, CommandError
from jinja2 import Environment, FileSystemLoader


class Command(BaseCommand):
    help = 'Application scaffold'

    def add_arguments(self, parser):
        parser.add_argument('app', nargs=1, type=str)
        parser.add_argument('model', nargs=1, type=str)
        parser.add_argument('output-file-path', default='/tmp/test.py', nargs=1, type=str)
        parser.add_argument(
            '--template-dir',
            default='/app/scaffold/templates',
            help='Path to a tamplate directory.',
        )
        parser.add_argument(
            '--template-name',
            default='test.tempy',
            help='Name of template file.',
        )


    def handle(self, *args, **options):
        template_dir = options.get('template_dir')
        template_name = options.get('template_name')
        template_file = f"{template_dir}/{template_name}"
        output_path = options.get('output-file-path')[0]

        valid_input = self.validate(output_path, template_file)
        if valid_input:
            data = {
                'app': options.get('app')[0],
                'model': options.get('model')[0]
            }
            self.write(output_path, template_dir, template_name, **data)
        
        print(self.style.SUCCESS('Baking done'))

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
    
    def write(self, output_path, template_dir, template_name, **data):
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_name)

        with open(output_path, "w") as file:
            file.write(template.render(data))
