from django.shortcuts import render

# Create your views here.
from .models import Home_Image, Vimeo_Link


def home_view(request):
    context = {
        'home_image': Home_Image.objects.first().image.url,
        'vimeo_links': Vimeo_Link.objects.all()
    }
    return render(request, 'home.html', context)
