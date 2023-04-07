from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from OnlineShop import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('products.urls')),
    path('',include('contact_us.urls')),
    path('', include('carts.urls')),

    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='pages/home.html'), name='home')
]

if settings.IS_DEVELOPING:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
