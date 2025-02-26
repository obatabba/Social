from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank=True
    )

    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profile_images/', default='profile_images/default.jpg'
    )
    
    def __str__(self) -> str:
        return self.user.username
    

class Tweet(models.Model):
    user = models.ForeignKey(
        User,
        related_name='tweets', 
        on_delete=models.CASCADE
    )
    body = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='uploaded_images/', null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return f"By: {self.user.username} | {self.created_at:%Y-%m-%d %H:%M} | {self.body:.40}..."
    
    def likes_count(self):
        return self.likes.count()
