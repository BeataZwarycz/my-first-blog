from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comments
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentsForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #zwraca wyrenderowany szablon
    return render(request, 'blog/post_list.html', {'posts': posts})
 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comments.objects.filter(created_date__lte=timezone.now())
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentsForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
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


