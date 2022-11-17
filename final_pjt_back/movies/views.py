from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieListSerializer, GenreSerializer, MovieSerializer
from .models import Movie_Image, Movie, Keyword, Genre

# Create your views here.


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        mk = serializer.data['movie_key']

        # 스틸컷 딕셔너리 만들기
        img_serial = Movie_Image.objects.filter(movie_id=mk)
        img_ser_len = len(img_serial)
                    # REF  Post.objects.all().order_by('id') 쿼리셋에 order by 지정할 수 있음
        img_lst = []
        for im in range(img_ser_len):
            img_lst.append({ im : img_serial[im].image_path })
        sd = dict(serializer.data)
        sd.update(stil_images=img_lst)

        return Response(sd)

# discovery_movie
@api_view(['GET'])
def discovery_movie_list(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def discovery_movie(request, genre_pk):
    if request.method == 'GET':
        # 장르 테이블에서 역참조
        genre = Genre.objects.get(pk=genre_pk)
        seri = genre.movie_set.all()
        # 영화 obj 쿼리셋을 받아서 영화리스트 시리얼라이저 사용
        serializer = MovieListSerializer(seri, many=True)
        return Response(serializer.data)
