from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 100, null = False, blank = False)

    def __str__(self):
        return self.title

class Time(models.Model):
    hours = models.CharField('opened hours', max_length = 20, null = False, blank = False)

    def __str__(self):
        return self.hours

class Point(models.Model):
    name = models.CharField(max_length = 200, null = False, blank = False)
    category = models.ManyToManyField(Category)
    time = models.ManyToManyField(Time)
    description = models.TextField()
    latitude = models.CharField(max_length = 200, null = False, blank = False)
    longitude = models.CharField(max_length = 200, null = False, blank = False)
    image1 = models.ImageField(upload_to = 'food_point_images', null = False, blank = False)
    image2 = models.ImageField(upload_to = 'food_point_images', null = False, blank = False)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    update_date = models.DateTimeField('update date', auto_now=True)
    point_disponibility = models.BooleanField('disponibility', default=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

    def was_modificated_recently(self):
        return self.edit_date >= timezone.now() - datetime.timedelta(days=1)

class Post(models.Model):
    point = models.ForeignKey(Point, on_delete = models.CASCADE)
    post = models.TextField('comment')
    note = models.IntegerField('point note', null = False, blank = False)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)

    def __str__(self):
        return self.post

    def was_published_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

class Publicity(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='publicities', null = False, blank = False)
    url = models.URLField('publicity website url')
    pub_date = models.DateTimeField('publication date', auto_now_add=True)
    mod_date = models.DateTimeField('modification date', auto_now=True)
    publicity_disponibility = models.BooleanField('disponibility', default=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def was_modificated_recently(self):
        return self.mod_date >= timezone.now() - datetime.timedelta(days=1)
