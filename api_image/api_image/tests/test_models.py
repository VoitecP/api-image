from django.test import TestCase
from gallery.models import *
from api.factories import *
from django.core.exceptions import ValidationError

class TierTestCase(TestCase):

    def setUp(self):
        self.tiers=TierFactory.build_batch(5)

    def test_tier_creation(self):
        for tier in self.tiers:
            tier.save()
            self.assertIsNotNone(tier.id)

    def test_tier_model_validation(self):
        with self.assertRaises(ValidationError):
            tier=TierFactory(model="Tier-Error", make="Tier-maker")
            
   

