from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
        url(r'^$',views.ThoughtsView, name='thoughts'),
        url(r'^posts/$', views.PostListView.as_view(), name='list'),
        url(r'^post/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='detail'),
)
