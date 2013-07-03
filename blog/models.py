from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField('Post Title', max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField('Contents (Markup Supported)', blank=True, default='')
    description = models.TextField('Description', blank=True, default='')
    published = models.BooleanField('Do we publish it ?', default=True)
    enable_comments = models.BooleanField('Enable comments for it ?', default=True)
    author = models.ForeignKey(User, related_name="posts")

    class Meta:
        ordering = ['updated_at','title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return("blog:detail", (), {"slug":self.slug})
