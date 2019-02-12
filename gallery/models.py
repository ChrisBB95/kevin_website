import os
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Gallery_Image(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(
        upload_to="")
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.title


@receiver(models.signals.post_delete, sender=Gallery_Image)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(models.signals.pre_save, sender=Gallery_Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        try:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
        except ValueError:
            return False
