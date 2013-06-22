from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
)
