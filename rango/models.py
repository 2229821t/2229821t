from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    #For Python 2, use __unicode__ too
    def __str__(self):
        return self.name

class Page(models.Model):
    #ForeignKey allows to create one-to-many relationship
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default = 0)

    # For Python 2, use __unicode__ too
    def __str__(self):
        return self.title