from django.db import models
from django_images.models import Image


class Product(models.Model):
    pass


class ProductImage(Image):
    product = models.ForeignKey(Product, related_name='images')
