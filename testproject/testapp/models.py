from django.db import models
from django_images.models import Image


class Product(models.Model):
    class Meta:
        app_label = 'testapp'


class ProductImage(Image):
    product = models.ForeignKey(Product, related_name='images')

    class Meta:
        app_label = 'testapp'
