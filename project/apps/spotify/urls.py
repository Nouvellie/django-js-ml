from .views import (
    AuthURLAPIView,
    IsAuthenticated,
    spotify_callback,
)
from django.urls import path


urlpatterns = [
   
    path(
        'spotify/get-auth-url',
        AuthURLAPIView.as_view(),
        name = 'get_auth_url',
    ),	

    path(
        'spotify/redirect',
        spotify_callback,
        name = 'spotify_callback',
    ),

    path(
        'spotify/is-authenticated',
        IsAuthenticated.as_view(),
        name = 'is_authenticated',
    ),

]