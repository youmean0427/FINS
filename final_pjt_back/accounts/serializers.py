from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User,Feed
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
            "feed_like_user",
            "followers",
        ]
        read_only_fields = [
            "id",
            "password",
            "last_login",
        ]

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','followings')

class FeelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'
        read_only_fields = ['id', 'movie_id', 'user', 'feed_like_user']