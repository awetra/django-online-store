from django.contrib import admin

from .models import Cart, CartProduct, Order, OrderStatus, OrderProduct


admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderProduct)
