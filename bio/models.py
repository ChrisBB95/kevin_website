from django.db import models

# Create your models here.


class Bio(models.Model):
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    business_address = models.CharField(max_length=30)
    about_me = models.TextField(max_length=1000)

    def __str__(self):
        return 'Bio'
