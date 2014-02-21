import datetime

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from markdown import markdown
from typogrify.filters import typogrify


def markup(text):
    """ Markup plain text into fancy HTML"""
    return typogrify(markdown(text,
        lazy_ol=False,
        output_format='html5',
        extentions=['abbr',
            'condehilite',
            'fenced_code',
            'sane_lists',
            'smart_strong']))


class PublicPostManager(models.Manager):
    """Returns published post that are not in the future"""
    def published_post(self):
        return self.get_query_set().filter(status__gte=2, publish__lte=datetime.datetime.now())

# TODO
# Create a model manager to get Likes count on posts

class Category(models.Model):
    """Category model for posts."""
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
        return ('blog_category_detail', None, {'slug':self.slug})


class Post(models.Model):
    """ Post model."""
    STATUS_CHOICES = (
            (1, 'Draft'),
            (2, 'Public'),
        )
    title = models.CharField('Title', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    author = models.ForeignKey(User)
    content = models.TextField('Contents',
            help_text='Content of this post goes here.',
            blank=True, default='')
    content_html = models.TextField(editable=False, blank=True, default='')
    tease = models.TextField('teaser', 
            help_text='Description needed for "meta description".',
            blank=True, default='')
    status = models.PositiveIntegerField('Status', choices=STATUS_CHOICES, default=1)
    publish = models.DateTimeField('Publish', default=datetime.datetime.now)
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Modified', auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)
    enable_comments = models.BooleanField('Comments',
            help_text='Should I enable comments for it ?',
            default=True)

    objects = models.Manager()
    public_post = PublicPostManager()

    # TODO
    # get likes for posts

    class Meta:
        ordering = ['-publish']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markup(self.content)
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return('blog:detail', None, {'slug':self.slug})


# TODO
# Add likes on posts
class Like(models.Model):
    liked_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    liked_by = models.ForeignKey(User)


    class Meta:
        unique_together = ('post','liked_by')


    def __unicode__(self):
        return "%s was liked by %s" %(self.post, self.liked_by)

