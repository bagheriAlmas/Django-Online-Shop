from django.urls import path
from .views import contact_us_view
urlpatterns = [
    path('contact-us/',contact_us_view,name='contact-us')
]