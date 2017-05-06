from django.contrib import admin
from .models import Post, Category, Recipe, Order

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Order)

