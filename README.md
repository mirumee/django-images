django-images
=============

Unlike other popular thumbnailing solutions, this one keeps information
about existing thumbnails in the database. This is crucial for external
storages where checking for file's existence can either cost significant
amounts of time or money (think Amazon S3).

We've decided to only generate thumbnails on demand. When requesting an
URL for a thumbnail that does not yet exist, you will receive an URL to
a view that actually generates the thumbnail and then redirects the
browser to the proper URL.

We also force you to define all thumbnail options in Django settings so
you don't accidentally end up with hundreds copies of the same image in
300×300, 303×301, 301×305 just because the template author was too lazy
to check the other places.


Models
------

We supply an `Image` model that holds information about the image.

```python
# models.py
from django import models
from django_images.models import Image


class Product(models.Model):
    pass


class ProductImage(Image):

    product = models.ForeignKey(Product, related_name='images')
```


Settings
--------

`IMAGE_SIZES` controls the sizes and options:

```python
# settings.py
IMAGE_SIZES = {
    'normal': {
        'size': (500, 0),
        'quality': 85
    },
    'tiny_square': {
        'size': (100, 100),
        'crop': True
    }
}
```

Possible params are `size` (tuple of `(width, height)`, zero as either
means unrestricted), `crop` (defaults to `False`), `upscale` (defaults to
`False`) and `quality` (default is `None`, uses whatever input image's
quality was).

`IMAGE_PATH` controls the upload path of both images and thumbnails. The
default implementation will use paths like:

```
image/original/by-md5/7/d/7d7561de541093c04bb89c33468e88c0/file.jpg
```


Templates
---------

```html+django
{% import at_size from images %}

{% for image in product.images.all %}
    <img src="{{ image|at_size:"tiny_square" }}" alt="">
{% endfor %}
```


Updating from django-images <= 0.3
----------------------------------

The database schema has been changed in 0.4 release. To accomodate
existing installations south migrations have been provided.

When updating an existing installation to 0.4, migrations have to be synced
with database. It can be done by doing:

```
$ ./manage.py migrate django_images 0001 --fake
$ ./manage.py migrate django_images
```
