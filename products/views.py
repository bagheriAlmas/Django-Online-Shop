from django.shortcuts import render

from products.models import Banner


def banner_list_view(request):
    banners = Banner.objects.all().filter(is_enabled=True)
    context = {
        'banners': banners,
    }
    return render(request, 'pages/home.html', context)
