from django.urls import path
from .views import all_posts, protected

urlpatterns = [
    path('', all_posts, name="all_posts"),
    path('protected/', protected, name="protected")
]