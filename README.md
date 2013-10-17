django-images
=============

Unlike other popular thumbnailing solutions, this one keeps information
about existing thumbnails in the database. This is crucial for external
storages where checking for file's existence can either cost significant
amounts of time or money (think Amazon S3).


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
