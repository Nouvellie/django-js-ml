from .views import FirstApiView
from django.urls import path


urlpatterns = [
    path(
        '',
        FirstApiView.as_view(),
        name = "first",
    ),	
]
