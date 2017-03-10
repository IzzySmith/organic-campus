from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class About(models.Model):
    #the About form has a title and some text input
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='static/img/images',
                              blank=True,
                              null=True)
    def publish_About(self):
        self.save()
