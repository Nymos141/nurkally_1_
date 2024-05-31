from django.urls import path
from .views import registration_api_view, AuthorizationAPIView, confirm_user_view

urlpatterns = [
    path('register/', registration_api_view, name='user-register'),
    path('login/', AuthorizationAPIView.as_view(), name='user-login'),
    path('confirm/', confirm_user_view, name='user-confirm'),
]
