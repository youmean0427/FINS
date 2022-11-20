from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import UserDetailsSerializer
from rest_framework.decorators import api_view
from .models import User

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailsSerializer()

@api_view(['GET'])
def user_info(request, username):
    user = User.objects.get(username=username)
    # 유저가 좋아요한 영화 
    print(user.username)
    result = {
        'id' : user.id,
        'username' : user.username,
        'email' : user.email,
        'profile_img' : user.profile_img,
    }
    return Response(result)

@api_view(['GET'])
def is_user(request, username):
    user = User.objects.filter(username=username) #get이 아니라 filter를 사용해야 값이 없어도 에러가 나지 않는다
    if not user : isUser = False
    else: isUser =True
    data = {
        'isUser' : isUser
    }
    return Response(data)
