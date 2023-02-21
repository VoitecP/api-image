from django.core.management.base import BaseCommand, CommandError
# from django.conf import settings
from django.core.management import call_command
import json

class Command(BaseCommand):
    args = ''
    help = 'Loader initial data in to database'
    def handle(self, *args, **options):
        call_command('loaddata',
                    'gallery/fixtures/tiers_data.json', 
                    verbosity=0,
                    # commit=False
                    )
        # another command
        result = {'message': "Successfully Loading initial data"}
        return json.dumps(result)