from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

slug = models.SlugField(blank=True)
slug = models.SlugField(unique=True)
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    #For Python 2, use __unicode__ too
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=128, unique = True)
    course = models.CharField(max_length=128, unique = True)


    class Meta:
        verbose_name_plural = "Subject"

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

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to = 'profile_images', blank = True)
    def __str__(self):
        return self.user.username