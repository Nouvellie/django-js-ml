from .views import (
    CreateRoomAPIView,
    GetRoomAPIView,
    JoinRoomView,
    RoomCreateView,
    RoomListView,
)
from django.urls import path


urlpatterns = [
    path(
        'apiroom/create',
        RoomCreateView.as_view(),
        name = 'room',
    ),
    
    path(
        'apiroom/list',
        RoomListView.as_view(),
        name = 'room',
    ),	

    path(
        'apiroom/create-room',
        CreateRoomAPIView.as_view(),
        name = 'create_room',
    ),	

    path(
        'apiroom/get-room',
        GetRoomAPIView.as_view(),
        name = 'get_room',
    ),	
    
    path(
        'apiroom/join-room',
        JoinRoomView.as_view(),
        name = 'join_room',
    ),	
]
