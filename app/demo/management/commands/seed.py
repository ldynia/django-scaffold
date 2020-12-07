import random
import string

from django.core.management.base import BaseCommand

from demo.models import DemoGroup


class Command(BaseCommand):
    help = 'Application seed'

    def add_arguments(self, parser):
        pass
   
    def handle(self, *args, **options):
        print(self.style.SUCCESS('Seeding start'))
        for _ in range(1000):
            charset = string.ascii_uppercase + string.digits
            name = ''.join(random.SystemRandom().choice(charset) for _ in range(5))
        
            DemoGroup.objects.get_or_create(name=name)
        
        print(self.style.SUCCESS('Seeding done'))