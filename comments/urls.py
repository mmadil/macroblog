from django.conf.urls.defaults import patterns, include, url
from . import views

urlpatterns = patterns('',
        url(r'^post/$', views.custom_post_comment, name='comments-post-comment'),
        url(r'', include('django.contrib.comments.urls')),
    )
