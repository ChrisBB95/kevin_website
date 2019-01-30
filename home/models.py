from django.db import models

# Create your models here.


class Home_Image(models.Model):
    image = models.ImageField(upload_to="photos/", blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)


class Vimeo_Link(models.Model):
    video = models.URLField()
