from .views import (
    FirstApiView,
    TestingView,
)
from django.urls import path


urlpatterns = [
    path(
        'first',
        FirstApiView.as_view(),
        name = 'first_api',
    ),	

    # Testing:
    path(
        '',
        TestingView.as_view(),
        name = 'first_view',
    ),
]
