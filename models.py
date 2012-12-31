from django.db import models


class File(models.Model):
    name = models.CharField(max_length=128)
    item = models.FileField(upload_to='files', verbose_name='file')
    date_uploaded = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        get_latest_by = '-date_uploaded'
        ordering = ('-date_uploaded',)

    def __unicode__(self):
        return self.item.name

    def get_absolute_url(self):
        return self.item.url
