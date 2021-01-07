import os

from django.core.management.base import BaseCommand

from config.settings import BASE_DIR
from leon.constants import SEQUENCE
from leon.utilities import animate


class DocsCommand(BaseCommand):
    
    help = "Leon API."

    def handle(self, *args, **options):
        animate(SEQUENCE, delay=0.2)
        
        print("Ultimate Code bakery!\n")
        
        os.system(f"python {BASE_DIR}/manage.py leon --help")