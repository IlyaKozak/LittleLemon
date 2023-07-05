from django.test import TestCase
from django.core import serializers

from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title='menu1', price=5.5, inventory=2)
        self.item2 = Menu.objects.create(title='menu2', price=7, inventory=18)

    def test_getall(self):
        menu1 = Menu.objects.get(title='menu1')
        menu2 = Menu.objects.get(title='menu2')

        self.assertEqual(str(menu1), 'menu1 : 5.50')
        self.assertEqual(str(menu2), 'menu2 : 7.00')