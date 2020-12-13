import os
import sys

from django.core.management.base import BaseCommand, CommandError

from config.settings import BASE_DIR
from leon.constants import SEQUENCE
from leon.utilities import animate


class DocsCommand(BaseCommand):
    help = "Leon CLI's API."

    def handle(self, *args, **options):
        animate(SEQUENCE, delay=0.3)
        print("Ultimate GraphQL API bakery!\n")
        os.system(f"python {BASE_DIR}/manage.py leon --help")