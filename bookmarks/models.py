# bookmarks/modeis.py

from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self): #추가
        return self.title if self.title else self.url
