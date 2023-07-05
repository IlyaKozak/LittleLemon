from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        menu_item = Menu.objects.create(title='ice cream', price=10, inventory=11)

        self.assertEqual(str(menu_item), 'ice cream : 10')
