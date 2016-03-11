# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_images', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('image_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='django_images.Image')),
                ('product', models.ForeignKey(related_name='images', to='testapp.Product')),
            ],
            bases=('django_images.image',),
        ),
    ]
