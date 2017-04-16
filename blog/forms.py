from django import forms

from .models import Post, Recipe

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'instructions')

