from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import UserDetailsSerializer,FeelListSerializer, FeedSerializer,FollowSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from movies.models import Movie_Image, Movie
import random
from .models import Feed

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailsSerializer()


# 랜덤한 하나의 이미지를 딕셔너리에 담아 반환하는 함수
def make_still(movie_id):
    img_serial = Movie_Image.objects.filter(movie_id=movie_id)
    img_ser_len = len(img_serial)
    if img_ser_len < 1:
        return '' 
    rannum = random.randrange(0, img_ser_len)
    stil_image = img_serial[rannum].image_path
    return stil_image

@api_view(['GET'])
def user_info(request, username):
    user = get_user_model().objects.get(username=username)
    serializer = UserDetailsSerializer(user)
    # print(serializer.data['like_movies'][0]['movie_key'])
    for i in range(len(serializer.data['like_movies'])):
        if 'movie_key' not in serializer.data['like_movies'][i]:
            serializer.data['like_movies'][i].update(movie_key='')
            continue
        mk = serializer.data['like_movies'][i]['movie_key']
        stil_image = make_still(mk)
        serializer.data['like_movies'][i].update(stil_image=stil_image)
    return Response(serializer.data)

@api_view(['GET'])
def is_user(request, username):
    user = get_user_model().objects.filter(username=username) #get이 아니라 filter를 사용해야 값이 없어도 에러가 나지 않는다
    if not user : isUser = False
    else: isUser =True
    data = {
        'isUser' : isUser
    }
    return Response(data)

@api_view(['POST'])
def follow(request, username):
    if request.user.is_authenticated:
        me = get_user_model()
        you = get_user_model().objects.filter(username=username)
        you = you[0]
        if me!= you:
            if you.followers.filter(pk=request.user.pk).exists():
                you.followers.remove(request.user)
                stts = '언팔로우'
            else:
                you.followers.add(request.user)
                stts = '팔로우'
        data = { 'status' : stts }
        return Response(data)
    return Response({'status' : '로그인이 필요합니다'}, status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def followinglist(request):
    user = get_user_model().objects.get(pk = request.user.pk)
    serializer = FollowSerializer(user)
    following_list = serializer.data['followings']
    result = []
    # print(user)
    for f in range(len(following_list)):
        nu = get_user_model().objects.get(pk = following_list[f])
        se = FollowSerializer(nu)
        # print(se.data['username'])
        result+= [se.data['username']]
    return Response(result)

@api_view(['GET'])
def feed_list(request,username):
    user = get_user_model().objects.get(username=username)
    # print(user.id)
    feeds = Feed.objects.filter(user=user.id)
    serializer = FeelListSerializer(feeds, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def feed_detail(request, feed_pk):
    feed = get_object_or_404(Feed, pk=feed_pk)
    if request.method == 'GET':
        serializer = FeedSerializer(feed)
        return Response(serializer.data)
    elif request.method == 'DELETE':
            # like(request, movie_pk) 함수 가져와서 
            # 좋아요 삭제
        seri = FeedSerializer(feed)
        movie = Movie.objects.get(pk=seri.data.get('movie_id')) 
        movie.movie_like_user.remove(request.user)
        feed.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = FeedSerializer(feed, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def feed_like(request, feed_pk):
    if request.user.is_authenticated:
        feed = Feed.objects.get(pk=feed_pk)
        liker = get_user_model().objects.get(pk=request.user.pk)
        if feed.feed_like_user.filter(pk=request.user.pk).exists():
            feed.feed_like_user.remove(request.user)
            stts = '좋아요 취소'
        else:
            feed.feed_like_user.add(request.user)
            stts = '좋아요'
        data = { 'status' : stts }
        return Response(data)
    return Response({'status' : '로그인이 필요합니다'}, status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def feed_like_check(request, feed_pk):
    if request.user.is_authenticated:
        feed = Feed.objects.get(pk=feed_pk)
        if feed.feed_like_user.filter(pk=request.user.pk).exists():
            stts = True
        else : 
            stts = False
        data = {'status' : stts}
        return Response(data)