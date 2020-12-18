from django.contrib import admin
from django.urls import (
    include,
    path,
)


urlpatterns = [
    # Admin:
    path('admin/', admin.site.urls),

    # Apps:
    path(
        '',
        include('apps.core.urls')
    ),
]