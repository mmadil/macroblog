from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class PublishedPost(models.Manager):
    def get_query_set(self):
        return super(PublishedPost, self).get_query_set().filter(published=True)


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

    class Meta:
        ordering = ['-updated_at','title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return("blog:detail", (), {"slug":self.slug})


class Tweet(models.Model):
    created_at = models.DateField(auto_now_add=True)
    content = models.TextField('Contents',
            help_text='Content of this tweet. 140 characters only.',
            max_length=140, unique=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-created_at']

    def __unicode__(self):
        return self.content


