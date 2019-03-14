from django.shortcuts import render
from bio.models import Bio

# Create your views here.
from .models import Home_Image, Vimeo_Link


def home_view(request):

    bio = Bio.objects.first()
    links = Vimeo_Link.objects.all()
    vimeo_links = [link.video[:8]+'player.'+link.video[8:18]+'video/'+link.video[18:]
                   for link in links]
    context = {
        'vimeo_links': vimeo_links,
        'bio': bio
    }

    if Home_Image.objects.exists():
        context['home_image'] = Home_Image.objects.first().image.url

    return render(request, 'home.html', context)


# link.video = https://vimeo.com/322787092

# desired https://player.vimeo.com/video/322787092
# for link in vimeo_links
#   link.video.insert(8,'player.').insert(25,'video/')
