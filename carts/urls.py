from django.urls import path
from .views import user_cart_view,create_cart_view
urlpatterns = [
    path('<int:pk>/cart/',user_cart_view,name='cart'),
    path('create/',create_cart_view,name='create-cart'),
]