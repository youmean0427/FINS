from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # user profile img 필드로 추가
    profile_img = models.CharField(max_length=1000)
    class Meta:
        db_table = 'user'

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    feed_like_user = models.ManyToManyField(User, related_name='feed_like_user')
