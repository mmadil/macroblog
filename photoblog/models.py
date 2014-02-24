import datetime

from django.db import models
from django.template.defaultfilters import slugify

class PublicPicsManager(models.Manager):
    """Returns published pictures that are not in the future."""
    def published_pictures(self):
        return self.get_query_set().filter(status__gte=2, publish__lte=datetime.datetime.now())


class Category(models.Model):
    """Categorizes pictures."""
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photoblog_category_detail', None, {'slug':self.slug})


class Picture(models.Model):
    """Post model for Photo Blog."""
    STATUS_CHOICES = (
            (1, 'Draft'),
            (2, 'Public'),
        )
    caption = models.CharField('Title', max_length=255, unique=True)
    image = models.FileField('Picture', upload_to='media', blank=True)
    credits = models.CharField('Credits', max_length=255, blank=True, default='')
    description = models.TextField('Description', blank=True, default='')
    status = models.PositiveIntegerField('Status', choices=STATUS_CHOICES, default=1)
    publish = models.DateTimeField('Publish', default=datetime.datetime.now)
    categories = models.ManyToManyField(Category, blank=True)
    enable_comments = models.BooleanField('Comments',
            default=False)
    objects = models.Manager()
    public_pics = PublicPicsManager()

    class Meta:
        ordering = ('-publish',)

    def __unicode__(self):
        return self.title


