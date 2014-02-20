import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.http.request import HttpRequest

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


class PublishedPost(models.Manager):
    def get_query_set(self):
        return super(PublishedPost, self).get_query_set().filter(published=True)

class Twitter(models.Manager):
    def get_query_set(self):
        pass

# TODO
# Create a model manager to get Likes count on posts

class Post(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    title = models.CharField('Title',
            help_text='',
            max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField('Contents',
            help_text='Content of this post goes here.',
            blank=True, default='')
    content_html = models.TextField(editable=False, blank=True, default='')
    description = models.TextField('Description', 
            help_text='Description needed for "meta description".',
            blank=True, default='')
    published = models.BooleanField('Publish',
            help_text='Can I publish it ?',
            default=False)
    enable_comments = models.BooleanField('Comments',
            help_text='Should I enable comments for it ?',
            default=True)
    author = models.ForeignKey(User)

    objects = models.Manager()
    published_post = PublishedPost()

    # TODO
    # get likes for posts

    class Meta:
        ordering = ['-updated_at','title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markup(self.body)
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return("blog:detail", (), {"slug":self.slug})


# TODO
# Add likes on posts
class Like(models.Model):
    liked_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    liked_by = models.URLField(blank=True, null=True, unique=True)


    class Meta:
        unique_together = ('post','liked_by')


    def __unicode__(self):
        return "%s was liked by %s" %(self.post, self.liked_by)

