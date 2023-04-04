from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView

from .views import data_list_view, product_detail_view

urlpatterns = [
    path('', data_list_view, name='banner'),
    path('product/<slug:slug>/', product_detail_view, name='product_detail'),
    path('about/', lambda request: render(request, 'pages/about.html'), name='about-us'),
    path('shop/', lambda request: render(request, 'pages/shop.html'), name='shop'),
]
