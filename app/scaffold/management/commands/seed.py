import os
import random
import string

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Application seed'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print(self.style.SUCCESS('Seeding start'))
        for i in range(1000):
            name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
            Group.objects.get_or_create(name=name)
        print(self.style.SUCCESS('Seeding done'))