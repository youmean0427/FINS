from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
from movies.serializers import MovieSerializer

class UserDetailsSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "last_login",
            "profile_img",
            "like_movies",
        ]
        read_only_fields = [
            "id",
            "password",
            "last_login",
        ]