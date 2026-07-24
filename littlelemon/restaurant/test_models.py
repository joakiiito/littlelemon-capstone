from decimal import Decimal
from django.test import TestCase
from django.utils import timezone

from .models import Menu, Booking


class MenuModelTest(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(title='Greek salad', price=Decimal('12.50'), inventory=100)
        self.assertEqual(item.title, 'Greek salad')
        self.assertEqual(item.price, Decimal('12.50'))
        self.assertEqual(item.inventory, 100)

    def test_menu_str(self):
        item = Menu.objects.create(title='Bruschetta', price=Decimal('7.00'), inventory=50)
        self.assertIn('Bruschetta', str(item))


class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name='Joaquin',
            no_of_guests=4,
            booking_date=timezone.now(),
        )
        self.assertEqual(booking.name, 'Joaquin')
        self.assertEqual(booking.no_of_guests, 4)

    def test_booking_str(self):
        booking = Booking.objects.create(
            name='Maria',
            no_of_guests=2,
            booking_date=timezone.now(),
        )
        self.assertIn('Maria', str(booking))
