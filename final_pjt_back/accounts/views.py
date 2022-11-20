from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import UserDetailsSerializer
from rest_framework.decorators import api_view
from rest_framework import status

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailsSerializer()

@api_view(['GET'])
def user_info(request, username):
    user = get_user_model().objects.filter(username=username)
    serializer = UserDetailsSerializer(user[0])
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