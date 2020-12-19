from .views import (
    FirstApiView,
    TestingView,
)
from django.urls import path


urlpatterns = [
    path(
        '',
        FirstApiView.as_view(),
        name = 'first_api',
    ),	

    # Testing:
    path(
        'home',
        TestingView.as_view(),
        name = 'first_view',
    ),
]
