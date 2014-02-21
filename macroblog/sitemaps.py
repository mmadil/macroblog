import datetime

from django.contrib.sitemaps import GenericSitemap

from blog.models import Post

post_dict = {
        'queryset': Post.objects.filter(status__gte=2, publish__lte=datetime.datetime.now()),
        'date_field': 'modified',
}

sitemaps = {
        'post': GenericSitemap(post_dict, priority=0.6),
}
