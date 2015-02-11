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


Installation
------------

You can install `django-images` using `pip`:

```
$ pip install django-images
```

Remember to add it to your project's `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = [
    ...,
    'django_images',
    ...
]
```

And to your `urls.py`:

```python
# urls.py
urlpatterns = patterns(
    '',
    ...,
    url(r'^images/', include('django_images.urls')),
    ...
)
```


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

You can override it by defining a function that accepts the model and
original filename and returns the path to use, as you would use with
Django `FileField`'s `upload_to` parameter. The main difference is that
the same function will be called for both original images and thumbnails:

```python
from django_images.models import Image

def my_image_path(instance, filename):
    if isinstance(instance, Image):
        return 'original/%s' % (filename,)
    else:
        return 'thumbnail/%s/%s' % (instance.size, filename)

IMAGE_PATH = my_image_path
```

You can also choose to define your custom function in another module and
set `IMAGE_PATH` to its location:

```python
IMAGE_PATH = 'my_package.my_module.my_function_name'
```

`IMAGE_AUTO_DELETE` controls deletion of files from the storage.
Django doesn't delete these files by default, but we do.


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
