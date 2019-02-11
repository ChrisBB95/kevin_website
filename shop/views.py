from django.shortcuts import render

# Create your views here.
from .models import Product
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm


def shop_view(request):
    cart = {}
    if request.session.get('cart', {}):
        cart = request.session.get('cart', {})

    context = {
        'products': Product.objects.all(),
        'cart': cart,
        'cart_size': len(cart.items())
    }
    if len(cart.items()) > 0:
        context['cart_size'] = sum([value for key, value in cart.items()])

    return render(request, 'shop.html', context)


def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart.keys():
        cart[str(item_id)] = cart[str(item_id)]+1
    else:
        cart[str(item_id)] = 1
    request.session['cart'] = cart

    context = {
        'products': Product.objects.all(),
        'cart': cart,
        'cart_size': len(cart.items())
    }
    if len(cart.items()) > 0:
        context['cart_size'] = sum([value for key, value in cart.items()])

    return render(request, 'shop.html', context)


def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    for id, quantity in cart.items():
        products.append((Product.objects.get(item_id=id).title,
                         quantity,
                         Product.objects.get(item_id=id).price,
                         Product.objects.get(item_id=id).price*quantity,
                         id))

    context = {
        'cart': cart,
        'cart_size': len(cart.items()),
        'products': products,
        'total': sum([product[3] for product in products])
    }
    if len(cart.items()) > 0:
        context['cart_size'] = sum([value for key, value in cart.items()])

    return render(request, 'cart.html', context)


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    del cart[str(item_id)]
    request.session['cart'] = cart

    products = []
    for id, quantity in cart.items():
        products.append((Product.objects.get(item_id=id).title,
                         quantity,
                         Product.objects.get(item_id=id).price,
                         Product.objects.get(item_id=id).price*quantity,
                         id))

    context = {
        'cart': cart,
        'cart_size': len(cart.items()),
        'products': products,
        'total': sum([product[3] for product in products])
    }
    if len(cart.items()) > 0:
        context['cart_size'] = sum([value for key, value in cart.items()])

    return render(request, 'cart.html', context)


def add_one(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] += 1
    request.session['cart'] = cart

    products = []
    for id, quantity in cart.items():
        products.append((Product.objects.get(item_id=id).title,
                         quantity,
                         Product.objects.get(item_id=id).price,
                         Product.objects.get(item_id=id).price*quantity,
                         id))

    context = {
        'cart': cart,
        'cart_size': len(cart.items()),
        'products': products,
        'total': sum([product[3] for product in products])
    }
    if len(cart.items()) > 0:
        context['cart_size'] = sum([value for key, value in cart.items()])

    return render(request, 'cart.html', context)


def sub_one(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] -= 1

    if cart[str(item_id)] == 0:
        del cart[str(item_id)]
    request.session['cart'] = cart

    products = []
    for id, quantity in cart.items():
        products.append((Product.objects.get(item_id=id).title,
                         quantity,
                         Product.objects.get(item_id=id).price,
                         Product.objects.get(item_id=id).price*quantity,
                         id))

    context = {
        'cart': cart,
        'cart_size': len(cart.items()),
        'products': products,
        'total': sum([product[3] for product in products])
    }
    if len(cart.items()) > 0:
        context['cart_size'] = sum([value for key, value in cart.items()])

    return render(request, 'cart.html', context)
