from django.db import models

class Quote(models.Model):
    quotation = models.TextField('Quotation', max_length=255)
    quoted_by = models.CharField('Quoted By', max_length=255)
    use_it = models.BooleanField('Use it ?', default=False)

    class Meta:
        ordering = ['quoted_by']

    def __unicode__(self):
        return self.quotation


