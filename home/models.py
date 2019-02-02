from django.db import models
from django.db.models.signals import post_delete
from .utils import file_cleanup

# Create your models here.


class Home_Image(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(
        upload_to="", blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.title


class Vimeo_Link(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    video = models.URLField()

    def __str__(self):
        return self.title


post_delete.connect(file_cleanup, sender=Home_Image,
                    dispatch_uid="gallery.image.file_cleanup")
