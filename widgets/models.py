from django.db import models
from django.template.defaultfilters import slugify

class Quote(models.Model):
    quotation = models.TextField('Quotation', max_length=255)
    quoted_by = models.CharField('Quoted By', max_length=255)
    use_it = models.BooleanField('Use it ?', default=False)

    class Meta:
        ordering = ['quoted_by']

    def __unicode__(self):
        return self.quotation


class Category(models.Model):
    """Categorizes bookmarks."""
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('bookmark_category_detail', None, {'slug':self.slug})


class Bookmark(models.Model):
    """Bookmark model for links."""
    STATUS_CHOICES = (
            (1,'Draft'),
            (2,'Public'),
        )
    title = models.CharField('Title', max_length=255)
    link = models.URLField('URL')
    tease = models.TextField('Teaser', blank=True, default='')
    status = models.PositiveIntegerField('Status', choices=STATUS_CHOICES, default=1)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

