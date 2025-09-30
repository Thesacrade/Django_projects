from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import CreatePost



# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') 
    return render(request, 'posts/posts_list.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required(login_url='/user/login/')
def new_post(request):
    if request.method == "POST":
        post = CreatePost(request.POST, request.FILES)
        if post.is_valid():
            newPost = post.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return redirect('posts')
    else:
        post = CreatePost()   
    return render(request, 'posts/new_post.html', {'post': post})