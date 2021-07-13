from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser


class BlogUserCreationForm(UserCreationForm):

    class Meta:
        model = BlogUser
        fields = ("username", "is_paid_subscriber")


class LoginBlogUser(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())