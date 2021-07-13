from django.contrib import auth
from django.shortcuts import render, redirect, reverse
from .forms import BlogUserCreationForm, LoginBlogUser
from django.contrib.auth import authenticate, login, logout

def signup_user(request):
    if request.method == "POST":
        form = BlogUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect( reverse('all_posts'))
    if request.method == "GET":
        form = BlogUserCreationForm()
        return render(request, 'userauth/signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = LoginBlogUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            valid_user = authenticate(username=username, password=password)
            if valid_user:
                login(request, valid_user)
                return redirect( reverse('all_posts'))
            else:
                return redirect( reverse('login_user'))
    if request.method == "GET":
        form = LoginBlogUser()
        return render(request, 'userauth/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect( reverse('login_user'))