from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .models import Post, Category, Recipe, Order
from .forms import PostForm, RecipeForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

def home(request):
    return render(request, 'blog/home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            #we save the form
            post = form.save(commit=True)
            post.author = request.user
            #set default publish date to this timezone
            post.published_date = timezone.now()
            #save the post
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'blog/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'blog/recipe_detail.html', {'recipe': recipe})

def recipe_new(request):
    form = RecipeForm()
    return render(request, 'blog/recipe_edit.html', {'recipe': recipe})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=post)
    if form.is_valid():
        recipe = form.save(commit=True)
        recipe.author = request.user
        recipe.save()
        return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=post)
    return render(request, 'recipe_edit.html', {'recipe': recipe})



"""
def recipe(request):
    recipe = Recipe.objects.all()
    return render(request, 'blog/recipe.html', {'recipes': recipe})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'blog/recipedetail.html', {'recipe': recipe})

def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            #we save the form
            recipe = form.save(commit=False)
            recipe.author = request.user
            #set default publish date to this timezone
            recipe.published_date = timezone.now()
            #save the post
            recipe.save()
            return redirect('recipedetail', pk=post.pk)
    else:
        form = RecipeForm()
    return render(request, 'blog/recipe_edit.html', {'form': form})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=post)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.published_date = timezone.now()
            recipe.save()
            return redirect('recipedetail', pk=post.pk)
    else:
        form = RecipeForm(instance=post)
    return render(request, 'blog/recipe_edit.html', {'form': form})

"""



# the contact view
def contact(request, pk):
    return render(request, 'blog/contact.html')

#the order view
def order(request):
    orders = Order.objects.all()
    return render(request, 'blog/order.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'blog/order_detail.html', {'order': order})

def order_new(request):
    order = OrderForm()
    return render(request, 'order/order_edit.html', {'order': order})
    
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)     
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=post)
    if order.is_valid():
        order = form.save(commit=True)
        order.author = request.user
        order.save()
        return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=post)
    return render(request, 'order_edit.html', {'order': order})

