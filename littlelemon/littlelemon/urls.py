from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser: user registration / management endpoints, e.g.
    #   POST /auth/users/            -> register a new user
    #   POST /auth/token/login/      -> obtain an auth token (djoser)
    #   POST /auth/token/logout/     -> invalidate the auth token
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # App routes (pages + API)
    path('', include('restaurant.urls')),
]
