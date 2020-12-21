from .views import IndexView
from django.urls import path


urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name = 'index_view',
    ),

    path(
        'join',
        IndexView.as_view(),
        name = 'join',
    ),
    
    path(
        'create',
        IndexView.as_view(),
        name = 'create',
    ),
 
    path(
        'room/<str:roomCode>',
        IndexView.as_view(),
        name = 'room_created',
    ),
]
