from .views import (
    FashionMnistAPIView,
)
from django.urls import path

urlpatterns = [
    path(
        'tflite/fashion-mnist',
        FashionMnistAPIView.as_view(),
        name = 'fashion_mnist',
    ),
]