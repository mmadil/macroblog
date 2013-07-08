from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin

admin.autodiscover()

from . import views
from .sitemaps import sitemaps
from biodata.views import BiodataListView, ProjectListView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
)

urlpatterns += patterns('',
    url(r'^$', views.IndexView, name='home'),
    url(r'^about/$', BiodataListView.as_view(), name='biolist'),
    url(r'^projects/$', ProjectListView.as_view(), name='projectlist'),
)

urlpatterns += patterns('',
        url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
#        url(r'favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
)

urlpatterns += patterns('',
        url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', { 'sitemaps': sitemaps}),
)
