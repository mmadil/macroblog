from django.contrib.sitemaps import GenericSitemap
from blog.models import Post

post_dict = {
        'queryset': Post.objects.filter(published=True),
        'date_field': 'updated_at',
}

sitemaps = {
        'post': GenericSitemap(post_dict, priority=0.6),
}
