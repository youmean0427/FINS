from rest_framework import serializers
from .models import Review, Movie_Image, Movie, Genre

# class MovieSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comment_set = CommentSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

#     class Meta:
#         model = Movie
#         fields = '__all__'

class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_Image
        fields = ('image_path')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('write_user', 'content', 'created_at', 'review_like_user' )

# Detail
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True )
    class Meta:
        model = Movie
        fields = '__all__'


