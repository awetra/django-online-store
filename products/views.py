from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Category, Product


def all_products_list(request):
    sales_products = Product.objects.filter(discount__gt=0)[:4]
    category_products = [category.products.all()[:4] for category in Category.objects.all()]
    for products in category_products:
        products.category = products[0].category
    
    context_data = {
        'sales_products': sales_products,
        'category_products': category_products
    }
    return render(request, 'products/all_products_list.html', context_data)


def products_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    paginator = Paginator(category.products.all(), 8)
    number_page = request.GET.get('page', 1)

    try:
        category_products = paginator.page(number_page)
    except EmptyPage:
        raise Http404
    
    context_data = {
        'category': category,
        'category_products': paginator.page(number_page)
    }
    return render(request, 'products/products_list_by_category.html', context_data)


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context_data = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context_data)