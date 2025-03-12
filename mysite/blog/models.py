from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(default='no desc.')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    #subtitle = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name="post_category")

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title
    
