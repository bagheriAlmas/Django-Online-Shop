from django.urls import path
from .views import data_list_view, product_detail_view

urlpatterns = [
    path('', data_list_view, name='banner'),
    path('product/<slug:slug>/', product_detail_view, name='product_detail')
]
