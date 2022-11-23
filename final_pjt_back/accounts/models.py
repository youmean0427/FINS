from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from movies.models import Movie

class UserManager(BaseUserManager):
    def create_user(self, email, password, username, **kwargs):
        if not username:
            raise ValueError('이름을 입력해야합니다. from backend..') #username을 필수로 입력받음
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # user profile img 필드로 추가
    profile_img = models.ImageField(upload_to="profile", blank=True, null=True)


    class Meta:
        db_table = 'user'

class Feed(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=100000)
    content = models.CharField(max_length=1000, null=True, blank=True)
    movie_id = models.IntegerField()
    feed_like_user = models.ManyToManyField(User, related_name='feed_like_user')
    class Meta:
        db_table = 'feed'
