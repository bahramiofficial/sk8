from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name","last_name","mobile","maker", "email" , "username"]


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "last_name", "mobile", "maker", "email", "username"]



class UserRetrieveTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "last_name", "mobile", "maker", "email", "username","term"]