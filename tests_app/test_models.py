from django.test import TestCase
from Littlelemon_Restaurant.models import *


class menuitemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title = 'IceCream',Price = 80,Inventory = 10)
        itemstr = item.get_item()
        self.assertEqual(itemstr,"IceCream : 80")