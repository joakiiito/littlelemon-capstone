from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def home(request):
    return render(request, 'index.html')


class MenuViewSet(viewsets.ModelViewSet):
    """
    Browsable API for the restaurant menu.

    GET    /api/menu/        -> list all menu items (open to everyone)
    POST   /api/menu/        -> create a menu item (authenticated users only)
    GET    /api/menu/{id}/   -> retrieve a single item
    PUT    /api/menu/{id}/   -> update an item (authenticated)
    DELETE /api/menu/{id}/   -> delete an item (authenticated)
    """
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    """
    Browsable API for table bookings. Requires authentication (token or
    session) for every action, since bookings are user-specific.

    GET    /api/bookings/        -> list all bookings
    POST   /api/bookings/        -> create a booking
    GET    /api/bookings/{id}/   -> retrieve a single booking
    PUT    /api/bookings/{id}/   -> update a booking
    DELETE /api/bookings/{id}/   -> delete a booking
    """
    queryset = Booking.objects.all().order_by('booking_date')
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
