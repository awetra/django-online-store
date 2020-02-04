from django.shortcuts import render, redirect
from django.urls import reverse


def add_basket_product(request):
    # if request.is_ajax():
    if request.session.session_key is None:
        request.session.save()
    session_key = request.session.session_key

    return redirect(reverse('products_list', kwargs={'category_slug': 'phones'}))