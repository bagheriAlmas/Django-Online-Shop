from django.shortcuts import render, get_object_or_404

from products.models import Banner, Category, Product


def data_list_view(request):
    banners = Banner.objects.all().filter(is_enabled=True)
    categories = Category.objects.all().filter(highlight=True)
    featured = Product.objects.all().filter(featured=True)
    context = {
        'banners': banners,
        'categories': categories,
        'featured': featured,
    }
    return render(request, 'pages/home.html', context)


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.all().filter(featured=False)[:10]
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'pages/product_detail.html', context)


def category_list_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'pages/shop.html', context)
