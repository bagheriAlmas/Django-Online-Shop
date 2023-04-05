from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView

from .views import data_list_view, product_detail_view, category_list_view

urlpatterns = [
    path('', data_list_view, name='banner'),
    path('product/<slug:slug>/', product_detail_view, name='product_detail'),
    path('about/', lambda request: render(request, 'pages/about.html'), name='about-us'),
    path('shop/', category_list_view, name='shop'),
]
