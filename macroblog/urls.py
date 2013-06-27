from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

from . import views
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
        url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
)
