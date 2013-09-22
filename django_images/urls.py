from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^thumbnail/(?P<image_id>\d+)/(?P<size>[^/]+)/$', views.thumbnail, name='image-thumbnail'),
)
