from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = get_user_model()
        fields = [
            "id",
            "username",
            "is_superuser",
            "email",
            "password",
            "first_name",
            "last_name",
            "date_joined",
            "last_login",
            "profile_img",
        ]
        read_only_fields = [
            "id",
            "is_superuser",
            "password",
            "date_joined",
            "last_login",
        ]