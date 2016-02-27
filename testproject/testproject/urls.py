from django.conf.urls import include, url


urlpatterns = [
    url(r'^images/', include('django_images.urls')),
    url(r'^.*$', 'testapp.views.index', name='index'),
]
