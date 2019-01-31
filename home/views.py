from django.shortcuts import render

# Create your views here.
from .models import Home_Image


def home_view(request):
    context = {
        'home_image': Home_Image.objects.first()

    }
    return render(request, 'home.html', context)
