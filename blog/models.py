from django.contrib.auth.models import User
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

class Order(models.Model):
    text = models.TextField()
    
    def publish(self):
        self.save()
    
    def __str__(self):
        return self.text

class Category(models.Model):
   """
   taken from the tutorial opentechschool.github.io
   this model describes a recipe category
   """
   name = models.CharField(u'Name', max_length=100)
   description = models.TextField(u'Description', blank=True)

   def __unicode__(self):
       return self.name


class Recipe(models.Model):
    CATEGORY_SOUP = 'SOUP'
    CATEGORY_PASTA = 'PASTA'
    CATEGORY_DESSERT = 'DESSERT'
    CATEGORY_SALAD = 'SALAD'
    CATEGORY_STEW = 'STEW'
    CATEGORIES = (
        (CATEGORY_SOUP, u'soup'),
        (CATEGORY_PASTA, u'pasta'),
        (CATEGORY_DESSERT, u'dessert'),
        (CATEGORY_SALAD, u'salad'),
        (CATEGORY_STEW, u'stew'),
    )
    DIFFICULTY_EASY = 'EASY'
    DIFFICULTY_MEDIUM = 'MEDIUM'
    DIFFICULTY_HARD = 'HARD'
    DIFFICULTIES = (
        (DIFFICULTY_EASY, u'easy'),
        (DIFFICULTY_MEDIUM, u'normal'),
        (DIFFICULTY_HARD, u'hard'),
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    time = models.IntegerField(blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.ManyToManyField(Category, verbose_name=u'Categories')
    figure = models.ImageField(upload_to="static/img",
                               blank=True,
                               null=True,
                               verbose_name="figure")
    difficulty = models.CharField(
       max_length=6,
       choices=DIFFICULTIES,
       default=DIFFICULTY_EASY,
    )
    categories = models.CharField(
       max_length=7,
       choices=CATEGORIES,
       default=CATEGORY_SOUP,
    )
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
