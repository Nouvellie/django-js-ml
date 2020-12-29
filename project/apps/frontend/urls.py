from .views import IndexView
from django.urls import path

app_name = 'frontend'

urlpatterns = [
    path(
        'room',
        IndexView.as_view(),
        name = 'index_view',
    ),

    path(
        'room/join',
        IndexView.as_view(),
        name = 'join',
    ),
    
    path(
        'room/create',
        IndexView.as_view(),
        name = 'create',
    ),
 
    path(
        'room/<str:roomCode>',
        IndexView.as_view(),
        name = 'room_created',
    ),
]
