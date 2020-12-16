import random

from django.core.management.base import BaseCommand

from demo.models import Dummy

WEEKDAY = (
    'Monday', 'Tuesday',
    'Wednesday', 'Thursday', 
    'Friday', 'Saturday', 'Sunday'
)

MONTH = (
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December'
)

class Command(BaseCommand):
    help = 'Application seed'

    def add_arguments(self, parser):
        pass
   
    def handle(self, *args, **options):
        print(self.style.SUCCESS('Seeding start'))
        
        for _ in range(1000):
            d = random.randint(1, 31)
            w = random.choice(WEEKDAY)
            m = random.choice(MONTH)
            y = random.randint(1800, 2020)

            Dummy.objects.get_or_create(pre_seeded=True, day=d, weekday=w, month=m, year=y)
        
        print(self.style.SUCCESS('Seeding done'))