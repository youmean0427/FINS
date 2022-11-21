from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import UserDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from movies.models import Movie_Image
import random

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