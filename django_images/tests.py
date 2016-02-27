import mock
import qrcode
from django.test import TestCase, override_settings
from django.core.files.images import ImageFile
from django.conf import settings
from django.utils.six import BytesIO
from django_images.models import Image, Thumbnail
from django.core.urlresolvers import reverse


class ImageModelTest(TestCase):
    def setUp(self):
        image_obj = BytesIO()
        qrcode_obj = qrcode.make('https://mirumee.com/')
        qrcode_obj.save(image_obj)
        self.image = Image.objects.create(width=370, height=370,
                                          image=ImageFile(image_obj, '01.png'))

    def test_get_by_size(self):
        size = settings.IMAGE_SIZES.keys()[0]
        thumb = Thumbnail.objects.get_or_create_at_size(self.image.id, size)
        self.image.get_by_size(size)

    def test_get_absolute_url(self):
        url = self.image.get_absolute_url()
        self.assertEqual(url, self.image.image.url)
        # For thumbnail
        size = settings.IMAGE_SIZES.keys()[0]
        thumb = Thumbnail.objects.get_or_create_at_size(self.image.id, size)
        url = self.image.get_absolute_url(size)
        self.assertEqual(url, thumb.image.url)
        # Fallback on creation url
        size = settings.IMAGE_SIZES.keys()[1]
        url = self.image.get_absolute_url(size)
        fallback_url = reverse('image-thumbnail', args=(self.image.id, size))
        self.assertEqual(url, fallback_url)


class ThumbnailModelTest(TestCase):
    def setUp(self):
        image_obj = BytesIO()
        qrcode_obj = qrcode.make('https://mirumee.com/')
        qrcode_obj.save(image_obj)
        self.image = Image.objects.create(width=370, height=370,
                                          image=ImageFile(image_obj, '01.png'))
        size = settings.IMAGE_SIZES.keys()[0]
        self.thumb = Thumbnail.objects.get_or_create_at_size(self.image.id, size)

    def test_get_absolute_url(self):
        url = self.thumb.get_absolute_url()
        self.assertEqual(url, self.thumb.image.url)


class PostSaveSignalOriginalChangedTestCase(TestCase):
    def setUp(self):
        image_obj = BytesIO()
        qrcode_obj = qrcode.make('https://mirumee.com/')
        qrcode_obj.save(image_obj)
        self.image = Image.objects.create(width=370, height=370,
                                          image=ImageFile(image_obj, '01.png'))
        size = settings.IMAGE_SIZES.keys()[0]
        self.thumb = Thumbnail.objects.get_or_create_at_size(self.image.id, size)

    def test_post_save_signal_original_changed(self):
        size = settings.IMAGE_SIZES.keys()[0]
        thumb = Thumbnail.objects.get_or_create_at_size(self.image.id, size)
        self.image.delete()
        self.assertFalse(Thumbnail.objects.exists())


class PostDeleteSignalDeleteImageFileTest(TestCase):
    def setUp(self):
        image_obj = BytesIO()
        qrcode_obj = qrcode.make('https://mirumee.com/')
        qrcode_obj.save(image_obj)
        self.image = Image.objects.create(width=370, height=370,
                                          image=ImageFile(image_obj, '01.png'))
        size = settings.IMAGE_SIZES.keys()[0]
        self.thumb = Thumbnail.objects.get_or_create_at_size(self.image.id, size)

    @override_settings(IMAGE_AUTO_DELETE=True)
    def test_post_delete_signal_delete_image_files_enabled(self):
        storage = self.image.image.storage
        image_name = self.image.image.name
        thumb_name = self.thumb.image.name
        self.image.delete()
        self.assertFalse(storage.exists(image_name))
        self.assertFalse(storage.exists(thumb_name))

    @mock.patch('django_images.models.IMAGE_AUTO_DELETE', False)
    def test_post_delete_signal_delete_image_files_disabled(self):
        storage = self.image.image.storage
        image_name = self.image.image.name
        thumb_name = self.thumb.image.name
        # Delete thumb
        self.thumb.delete()
        self.assertTrue(storage.exists(image_name))
        self.assertTrue(storage.exists(thumb_name))
        # Delete image
        self.image.delete()
        self.assertTrue(storage.exists(image_name))
        self.assertTrue(storage.exists(thumb_name))
