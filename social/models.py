from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField(blank=False, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)


class Like(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postLikes')


class Comment(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postComments')
