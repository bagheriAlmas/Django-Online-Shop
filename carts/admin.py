from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.
def total_price(obj):
    return obj.total_price


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ['user', 'factor_number', 'total_price', 'created', 'is_paid']
    inlines = [CartItemInline]


admin.site.register(Cart, CartAdmin)
