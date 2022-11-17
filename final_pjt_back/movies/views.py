from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieListSerializer, GenreSerializer
from .serializers import MovieSerializer, MovieImageSerializer
from .models import Movie_Image, Movie, Genre

# Create your views here.


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    print(movie.genres.all())
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def movie_genre(request, movie_pk):
    genre = Genre.objects.get(movie_pk = movie_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)