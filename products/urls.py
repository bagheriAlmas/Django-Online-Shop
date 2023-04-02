from django.urls import path
from .views import banner_list_view
urlpatterns = [
    path('',banner_list_view,name='banner')
]
