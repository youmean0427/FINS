from rest_framework import serializers
from .models import Review, Movie, Genre, Keyword


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        # fields = ('genre_name',)

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview',)

class ReviewSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(source='user.user_id', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','id','write_user','review_like_user',)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('write_user', 'content', 'created_at', 'review_like_user' )

# Detail
class MovieSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True )
    class Meta:
        model = Movie
        fields = '__all__'


