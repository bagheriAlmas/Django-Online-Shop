from django.shortcuts import render

from products.models import Banner, Category, Product


def data_list_view(request):
    banners = Banner.objects.all().filter(is_enabled=True)
    categories = Category.objects.all().filter(highlight=True)
    featured = Product.objects.all().filter(featured=True)
    context = {
        'banners': banners,
        'categories':categories,
        'featured' : featured,
    }
    return render(request, 'pages/home.html', context)
