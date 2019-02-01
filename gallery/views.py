from django.shortcuts import render

# Create your views here.
from .models import Gallery_Image


def gallery_view(request):
    context = {
        'gallery_images': Gallery_Image.objects.all()
    }
    return render(request, 'gallery.html', context)
