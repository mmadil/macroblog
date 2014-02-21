import datetime

from django.db import models

class PublicPicsManager(models.Manager):
    """Returns published pictures that are not in the future."""
    def published_pictures(self):
        return self.get_query_set().filter(status__gte=2, publish__lte=datetime.datetime.now())


class Category(models.Model):
    """Categorizes pictures."""
    

class Picture(models.Model):
    """Post model for Photo Blog."""
    STATUS_CHOICES = (
            (1, 'Draft'),
            (2, 'Public'),
        )
    caption = models.CharField('Title', max_length=255, unique=True)
    description = models.TextField('Description', blank=True, default='')
    status = models.PostiveIntegerField('Status', choices=STATUS_CHOICES, default=1)
    publish = models.DateTimeField('Publish', default=datetime.datetime.now)
    categories = models.ManyToManyField(Categories, blank=True)
    enable_comments = models.BooleanField('Comments',
            default=False)
    objects = models.Manager()
    public_pics = PublicPicsManager()
