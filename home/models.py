import os
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
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


@receiver(models.signals.post_delete, sender=Home_Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Gallery_Image` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Home_Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Home_Image` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except Home_Image.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
