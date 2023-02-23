import factory
import pytest_django
import factory.fuzzy
from gallery.models import *

# from factory.faker import Faker

class TierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Tier
        # model='gallery.Tier'
    
    tier_type=5
    tier_name="Test-tier"
    thumb1_H=555
    thumb1_W=444
    thumb2_H=666
    thumb2_W=777

   

