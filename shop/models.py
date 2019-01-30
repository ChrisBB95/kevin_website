from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
