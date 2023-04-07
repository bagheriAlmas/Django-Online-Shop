from django.shortcuts import render

from users.models import CustomUser
from .models import Cart


# Create your views here.
def user_cart_list_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    carts = Cart.objects.all().filter(user=user)
    return render(request, 'pages/cart.html', {'carts': carts})


def create_cart_view(request):
    user = request.user
    carts = Cart.objects.all().filter(is_paid=False)
    if carts.count() == 0:
        cart = Cart(user=user, is_paid=False)
        cart.save()
        return render(request, 'pages/home.html', {})
    return render(request, 'pages/cart.html', {})
