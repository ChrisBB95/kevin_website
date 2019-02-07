from django.shortcuts import render

# Create your views here.
from .models import Product


def shop_view(request):

    context = {
        'products': Product.objects.all(),
    }

    if request.session.get('cart', {}):
        context['cart'] = request.session.get('cart', {})
    else:
        context['cart'] = {}

    return render(request, 'shop.html', context)


def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    if item_id in cart.keys():
        cart[item_id] += 1
    else:
        cart[item_id] = 1
    request.session['cart'] = cart

    context = {
        'products': Product.objects.all(),
        'cart': cart
    }

    return render(request, 'shop.html', context)


def view_cart(request):
    cart = request.session.get('cart', {})

    context = {
        'products': Product.objects.all(),
        'cart': cart
    }

    return render(request, 'shop.html', context)
