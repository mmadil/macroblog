from django.db import models

class Quote(models.Model):
    quotation = models.TextField('Quotation', max_length=255)
    quoted_by = models.CharField('Quoted By', max_length=255)
    use_it = models.BooleanField('Use it ?', default=False)

    class Meta:
        ordering = ['quoted_by']

    def __unicode__(self):
        return self.quotation

class Bookmark(models.Model):
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)
    title = models.CharField('Title', max_length=255)
    link = models.URLField('URL')
    description = models.TextField('Description', max_length=255)
    show = models.BooleanField('Display it ?', default=False)

    class Meta:
        ordering = ['-updated_at']

    def __unicode__(self):
        return self.title

