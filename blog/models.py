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


class Category(models.Model):
   """
   taken from the tutorial opentechschool.github.io
   this model describes a recipe category
   """
   name = models.CharField(u'Name', max_length=100)
   description = models.TextField(u'Description', blank=True)

   def __unicode__(self):
       return self.name

"""
class Recipe(models.Model):
   
    
   
    DIFFICULTY_EASY = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD = 3
    DIFFICULTIES = (
        (DIFFICULTY_EASY, u'easy'),
        (DIFFICULTY_MEDIUM, u'normal'),
        (DIFFICULTY_HARD, u'hard'),
    )
    title = models.CharField('Title', max_length=255)
    ingredients = models.TextField(u'Indigrents',
        help_text=u'One indigrent per line')
    preparation = models.TextField(u'Preparation')
    time_for_preparation = models.IntegerField(u'Preparation time',
        help_text=u'Time for preperation', blank=True, null=True)
    number_of_portions = models.PositiveIntegerField(u'Number of portions')
    difficulty = models.SmallIntegerField(u'Difficulty',
        choices=DIFFICULTIES, default=DIFFICULTY_MEDIUM)
   # category = models.ManyToManyField(Category, verbose_name=u'Categories')
    author = models.ForeignKey(User, verbose_name=u'Author')
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = u'Recipe'
        verbose_name_plural = u'Recipes'
        ordering = ['-date_created']

    def save(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
"""

class Recipe(models.Model):
    DIFFICULTY_EASY = 'EY'
    DIFFICULTY_MEDIUM = 'NL'
    DIFFICULTY_HARD = 'HD'
    DIFFICULTIES = (
        (DIFFICULTY_EASY, u'easy'),
        (DIFFICULTY_MEDIUM, u'normal'),
        (DIFFICULTY_HARD, u'hard'),
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.ManyToManyField(Category, verbose_name=u'Categories')
    figure = models.ImageField(upload_to="static/img",
                               blank=True,
                               null=True,
                               verbose_name="figure")
    difficulty = models.CharField(
       max_length=2,
       choices=DIFFICULTIES,
       default=DIFFICULTY_EASY,
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
