from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.home, name='home'),

    # DRF's built-in token endpoint, e.g.:
    #   POST /api-token-auth/  {"username": "...", "password": "..."}
    #   -> {"token": "..."}
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Menu + Booking APIs (browsable API at /api/)
    path('api/', include(router.urls)),
]
