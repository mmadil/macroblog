from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin

admin.autodiscover()

from . import views
from .sitemaps import sitemaps
from widgets.views import BookmarkListView

urlpatterns = patterns('',
    url(r'^manage-site/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^thoughts/', include('blog.urls', namespace='blog')),
)

urlpatterns += patterns('',
    url(r'^$', views.IndexView, name='home'),
    url(r'^bookmarks/$', BookmarkListView.as_view(), name='bookmarklist'),
)

urlpatterns += patterns('',
        url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
#       url(r'favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
        url(r'^(?P<url>.*/)$', 'flatpage'),
)

urlpatterns += patterns('',
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', { 'sitemaps': sitemaps}),
)
