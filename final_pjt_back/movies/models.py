from django.db import models
from django.conf import settings

class Keyword(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword_id = models.IntegerField()
    keyword = models.CharField(max_length=100)

    class Meta:
        db_table = 'keyword'


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=1000)
    
    class Meta:
        db_table = 'genre'
    

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    overview = models.TextField()
    popularity = models.FloatField()
    release_date = models.DateField(auto_now_add=True, null=True)
    vote_average = models.FloatField()
    movie_key = models.IntegerField()
    video_path = models.CharField(max_length=1000)
    poster = models.CharField(max_length=1000)

    genres = models.ManyToManyField(Genre)
    keyword = models.ManyToManyField(Keyword)
    movie_like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies') # 좋아요 테이블
    
    class Meta:
        db_table = 'movie'


class Movie_Image(models.Model):
    id = models.IntegerField(primary_key=True)
     # 영화 스틸컷
    image_path = models.CharField(max_length=1000)
    movie_id = models.IntegerField() # 영화의 movie_key

    class Meta:
        db_table = 'movie_image'


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    write_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'review'