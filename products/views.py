from django.shortcuts import render

from products.models import Banner, Category


def data_list_view(request):
    banners = Banner.objects.all().filter(is_enabled=True)
    categories = Category.objects.all().filter(highlight=True)
    context = {
        'banners': banners,
        'categories':categories,
    }
    return render(request, 'pages/home.html', context)
