from .views import (
    CreateRoomAPIView,
    GetRoomAPIView,
    JoinRoomAPIView,
    RoomCreateAPIView,
    RoomListAPIView,
    UserInRoomAPIView,
)
from django.urls import path


urlpatterns = [
    path(
        'apiroom/create',
        RoomCreateAPIView.as_view(),
        name = 'room',
    ),
    
    path(
        'apiroom/list',
        RoomListAPIView.as_view(),
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
        JoinRoomAPIView.as_view(),
        name = 'join_room',
    ),	
    
    path(
        'apiroom/user-in-room',
        UserInRoomAPIView.as_view(),
        name = 'user_in_room',
    ),	
]
