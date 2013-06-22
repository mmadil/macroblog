from django.db import models

class Biodata(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    heading = models.CharField('Heading', max_length=255)
    content = models.TextField('Biodata ( Markdown Supported )', max_length=500, blank=True, default='')
    published = models.BooleanField()