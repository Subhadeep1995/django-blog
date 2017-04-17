from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    context = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post':context})

def post_new(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)

    else:    
        form = PostForm()
        form_type = 'Create New Post'
        return render(request, 'blog/post_edit.html', {'form': form, 'form_type':form_type})


def post_delete(request, id):
    context = get_object_or_404(Post, id=id)
    context.delete()
    return redirect('post_list')