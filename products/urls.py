from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_products_list, name='all_products_list'),
    path('<slug:category_slug>/', views.products_list_by_category, name='products_list_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail')
]