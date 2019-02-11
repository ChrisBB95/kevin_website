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
                         Product.objects.get(item_id=key).price*value,
                         key))

    context['products'] = products
    context['total'] = sum([product[2] for product in products])

    return render(request, 'cart.html', context)


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    del cart[str(item_id)]
    request.session['cart'] = cart

    context = {
        'cart': cart
    }

    products = []
    for key, value in cart.items():
        products.append((Product.objects.get(item_id=key).title,
                         value,
                         Product.objects.get(item_id=key).price*value,
                         key))

    context['products'] = products
    context['total'] = sum([product[2] for product in products])

    return render(request, 'cart.html', context)


def add_one(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] += 1
    request.session['cart'] = cart

    context = {
        'cart': cart
    }

    products = []
    for id, quantity in cart.items():
        products.append((Product.objects.get(item_id=id).title,
                         quantity,
                         Product.objects.get(item_id=id).price*quantity,
                         id))

    context['products'] = products
    context['total'] = sum([product[2] for product in products])

    return render(request, 'cart.html', context)


def sub_one(request, item_id):
    cart = request.session.get('cart', {})
    cart[str(item_id)] -= 1

    if cart[str(item_id)] == 0:
        del cart[str(item_id)]
    request.session['cart'] = cart

    context = {
        'cart': cart
    }

    products = []
    for id, quantity in cart.items():
        products.append((Product.objects.get(item_id=id).title,
                         quantity,
                         Product.objects.get(item_id=id).price*quantity,
                         id))

    context['products'] = products
    context['total'] = sum([product[2] for product in products])

    return render(request, 'cart.html', context)


def checkout(request):
    cart = request.session.get('cart', {})

    checkout_cart = []
    for id, quantity in cart.items():
        checkout_cart.append((Product.objects.get(item_id=id).title,
                              quantity,
                              Product.objects.get(item_id=id).price*quantity))

    context = {
        'cart': checkout_cart
    }

    context['total'] = sum([item[2] for item in checkout_cart])
    return render(request, 'checkout.html', context)
