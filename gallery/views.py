from django.shortcuts import render

# Create your views here.
from .models import Gallery_Image
from bio.models import Bio


def gallery_view(request):
    bio = Bio.objects.first()
    context = {
        'gallery_images': Gallery_Image.objects.all(),
        'bio':bio
    }
    return render(request, 'gallery.html', context)
