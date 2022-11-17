from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),

    #discoveryMovie
    path('discoverymovie/', views.discovery_movie_list),
    path('discoverymovie/<int:genre_pk>/', views.discovery_movie),
]

