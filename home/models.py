from django.db import models


class Search(models.Model):
    objects = None
    search = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'
