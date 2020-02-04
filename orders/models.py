from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Cart(models.Model):
    session_key = models.CharField(max_length=128)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.session_key


class CartProduct(models.Model):
    quantity = models.PositiveIntegerField(blank=True, null=True, default=1)

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='products'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='basket_products'
    )

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'



class OrderStatus(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = 'Order statuses'

    def __str__(self):
        return self.name


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.ForeignKey(
        OrderStatus,
        null=True,
        on_delete=models.SET_NULL,
        related_name='orders'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    def __str__(self):
        return f'{self.customer.email} | {self.status.name} | {self.total_price}$'


class OrderProduct(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(blank=True, null=True, default=1)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='products'
    )
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
        related_name='order_products'
    )

    def __str__(self):
        return f'{self.name} | {self.price}$ | {self.quantity}x'