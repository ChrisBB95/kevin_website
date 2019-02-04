from django.shortcuts import render

# Create your views here.
from .models import Product


def shop_view(request):

    context = {
        'products': Product.objects.all()
    }

    return render(request, 'shop.html', context)
