from django.shortcuts import render

# Create your views here.
from .models import Home_Image, Vimeo_Link


def home_view(request):
    context = {
        'home_image': Home_Image.objects.first().image.url,
        'vimeo_link': Vimeo_Link.objects.first().video
    }
    return render(request, 'home.html', context)
