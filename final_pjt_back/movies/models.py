from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Keyword(models.Model):
    keyword = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=1000)
    overview = models.TextField()
    popularity = models.FloatField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    
    genres = models.ManyToManyField(Genre)
    keyword = models.ManyToManyField(Keyword)
    # 영화 포스터
    poster = models.CharField(max_length=1000)
   
class Movie_Image(models.Model):
     # 영화 스틸컷
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE) # 영화 id
    image_path = models.CharField(max_length=1000)
    

    movie_like_user = models.ManyToManyField(settings.AUTH_USER_MODEL) # 좋아요 테이블
#   keyword_ids VARCHAR
#   poster_ids VARCHAR
#   genre_ids VARCHAR

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    write_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_like_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='like_user')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)