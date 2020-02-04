from django.urls import path

from . import views


urlpatterns = [
    path('add_basket_product/', views.add_basket_product, name='add_basket_product')
]