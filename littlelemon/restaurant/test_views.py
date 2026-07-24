from decimal import Decimal
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Menu, Booking


class MenuViewSetTest(APITestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title='Greek salad', price=Decimal('12.50'), inventory=100)

    def test_list_menu_items_is_public(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item_requires_authentication(self):
        response = self.client.post('/api/menu/', {'title': 'Pasta', 'price': '15.00', 'inventory': 10})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class BookingViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joaquin', password='testpass123')
        self.token_url = '/api-token-auth/'

    def _authenticate(self):
        response = self.client.post(self.token_url, {'username': 'joaquin', 'password': 'testpass123'})
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

    def test_bookings_require_authentication(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_obtain_token(self):
        response = self.client.post(self.token_url, {'username': 'joaquin', 'password': 'testpass123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_create_booking_when_authenticated(self):
        self._authenticate()
        payload = {
            'name': 'Joaquin',
            'no_of_guests': 3,
            'booking_date': timezone.now().isoformat(),
        }
        response = self.client.post('/api/bookings/', payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_list_bookings_when_authenticated(self):
        self._authenticate()
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
