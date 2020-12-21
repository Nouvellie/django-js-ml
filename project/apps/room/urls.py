from .views import (
    CreateRoomAPIView,
    RoomCreateView,
    RoomListView,
)
from django.urls import path


urlpatterns = [
    path(
        'create',
        RoomCreateView.as_view(),
        name = 'room',
    ),
    
    path(
        'list',
        RoomListView.as_view(),
        name = 'room',
    ),	

    path(
        'create-room',
        CreateRoomAPIView.as_view(),
        name = 'create_room',
    ),	
]
