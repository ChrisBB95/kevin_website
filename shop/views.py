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
        'cart': cart
    }

    products = []
    for key, value in cart.items():
        products.append((Product.objects.get(item_id=key).title,
                         value,
                         Product.objects.get(item_id=key).price,
                         key))

    context['products'] = products
    context['total'] = sum([product[2] for product in products])

    return render(request, 'cart.html', context)


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    del cart[item_id]
    request.session['cart'] = cart

    context = {
        'cart': cart
    }

    products = []
    for key, value in cart.items():
        products.append((Product.objects.get(item_id=key).title,
                         value,
                         Product.objects.get(item_id=key).price,
                         key))

    context['products'] = products
    context['total'] = sum([product[2] for product in products])

    return render(request, 'cart.html', context)
