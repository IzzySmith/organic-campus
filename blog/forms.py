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

class ContactForm(forms.Form):
    contact_name= forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
)
