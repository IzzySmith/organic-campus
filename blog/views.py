from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .models import Post
from .forms import PostForm

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
            post = form.save(commit=False)
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
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def about(request):
    if request.method=='POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
           image = about.objects.get(pk=course_id)
           image.model_pic = form.cleaned_data['image']
           image.save()
    return render(request, 'blog/about.html', {'about': about})
