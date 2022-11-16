from django.contrib import admin
from movies.models import Movie, Keyword, Movie_Image, Review, Genre



# Register your models here.
admin.site.register(Movie)
admin.site.register(Keyword)
admin.site.register(Genre)
admin.site.register(Movie_Image)
admin.site.register(Review)