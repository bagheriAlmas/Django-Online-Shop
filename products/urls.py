from django.urls import path
from .views import data_list_view
urlpatterns = [
    path('',data_list_view,name='banner')
]
