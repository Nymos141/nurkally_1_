from django.urls import path
from .views import (registration_api_view, AuthorizationAPIView, confirm_user_view,
                    RegistrationAPIView, AuthorizationAPIView, ConfirmUserView)

urlpatterns = [
    path('register/', registration_api_view, name='user-register'),
    path('login/', AuthorizationAPIView.as_view(), name='user-login'),
    path('confirm/', confirm_user_view, name='user-confirm'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('authorization/', AuthorizationAPIView.as_view(), name='authorization'),
    path('confirm/', ConfirmUserView.as_view(), name='confirm'),
]
