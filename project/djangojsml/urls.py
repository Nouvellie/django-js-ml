from django.contrib import admin
from django.urls import (
    include,
    path,
)


api_urlpatterns = [
    path(
        'accounts/', 
        include('rest_registration.api.urls'),
    ),
]

urlpatterns = [
    # Admin:
    path(
        'nouvellie-admin/', 
        admin.site.urls,
    ),

    # Core app:
    path(
        '',
        include('apps.core.urls'),
    ),

    # Apps:
    path(
        'api/',
        include('apps.apiregistration.urls'),
    ),

    # DRF Registration:
    path(
        'api/v1/', 
        include(api_urlpatterns),
    ),
]