from django.urls import path
from .views import UserRegisterView, user_detail_view

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),
    path('profile', user_detail_view, name='user_profile')
]
