from rest_framework import serializers
from .models import Review, Movie, Genre, Keyword, Movie_Image


class GenreSerializer(serializers.ModelSerializer):
    movie_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = '__all__'
        # fields = ('genre_name',)

class KeywordSerializer(serializers.ModelSerializer):
    movie_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Keyword
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ('id', 'title', 'overview','movie_key', 'vote_average')
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.IntegerField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'content', 'username', 'created_at')
        read_only_fields = ('movie','id','write_user','review_like_user',)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'write_user', 'content', 'created_at', 'review_like_user' )

# Detail
class MovieSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True )
    class Meta:
        model = Movie
        fields = '__all__'

class StillImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Image
        fields = '__all__'

