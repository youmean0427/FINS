from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/genre', views.movie_genre),

]

