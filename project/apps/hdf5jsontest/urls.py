from .views import (
    Test,
)
from django.urls import path


urlpatterns = [
    path(
        'hdf5json/test',
        Test.as_view(),
        name = 'test',
    ),	
]