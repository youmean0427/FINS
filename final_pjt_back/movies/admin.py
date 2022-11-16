from django.contrib import admin
from movies.models import Movie, Genre, Keyword, Movie_Image, Review


# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Keyword)
admin.site.register(Movie_Image)
admin.site.register(Review)