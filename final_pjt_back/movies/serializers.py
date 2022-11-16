from rest_framework import serializers
from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview',)

# class MovieSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comment_set = CommentSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

#     class Meta:
#         model = Movie
#         fields = '__all__'
