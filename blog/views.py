from django.shortcuts import render, redirect, reverse
from .models import BlogPost


def all_posts(request):
    posts = BlogPost.objects.all().exclude(id=3)
    return render(request, 'blog/all.html', {'posts': posts})


def protected(request):
    if request.user.is_authenticated:
        post = BlogPost.objects.get(id=3)
        return render(request, 'blog/secret.html', {'post': post})
    else:
        return redirect( reverse('login_user'))