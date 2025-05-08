from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, ActivityForm
from .models import Post


# Create your views here.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts_page')
    else:
        form = PostForm()
    return  render(request, 'postings/create_post.html', {'form': form})

def posts_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,'postings/posts_page.html',{'posts':posts})

@login_required
def create_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('home')
    else:
        form = ActivityForm()
    return render(request, 'postings/create_activity.html',{'form': form})



