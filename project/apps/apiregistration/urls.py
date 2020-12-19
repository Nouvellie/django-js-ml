from .views import (
    ResetPasswordView,
    VerifyRegistrationView,
)
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # JWT:
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Registration's View:
    path(
        'accounts/reset-password/',
        ResetPasswordView.as_view(),
        name='reset_password',
    ),
    
    path(
        'accounts/verify-registration/',
        VerifyRegistrationView.as_view(),
        name='verify_registration',
    ),
]
