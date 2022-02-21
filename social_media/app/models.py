from typing import cast
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField()
    # date = models.DateField(auto_now_add=True, null=True)
    # date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.user} + {self.caption[:20]}"

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    followers = models.IntegerField()
    following = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return str(self.user)

class Like(models.Model):
    user = models.ManyToManyField(User)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0) 
    
class Comments(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)
    
