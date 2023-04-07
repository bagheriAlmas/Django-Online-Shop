import uuid
from random import randint

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from products.models import Product
from users.models import CustomUser


# Create your models here.


class Cart(models.Model):
    factor_number = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            total += (cart_item.price * cart_item.quantity)
        return int(total)

    def __str__(self):
        return self.user.username


@receiver(pre_save, sender=Cart)
def set_factor_number(sender, instance, *args, **kwargs):
    rand = randint(11111111, 99999999)
    instance.factor_number = slugify(instance.user.username + "-" + str(rand))


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveSmallIntegerField()

    @property
    def total_price(self):
        return int(self.price * self.quantity)

    def __str__(self):
        return self.product.name
