import random
import string

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
            charset = string.ascii_uppercase + string.digits
            name = ''.join(random.SystemRandom().choice(charset) for _ in range(5))
            
            weekday = random.choice(WEEKDAY)
            month = random.choice(MONTH)
            year = random.randint(1800, 2020)

            Dummy.objects.get_or_create(name=name, weekday=weekday, month=month, year=year)
        
        print(self.style.SUCCESS('Seeding done'))