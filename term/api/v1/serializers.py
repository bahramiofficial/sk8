from rest_framework import serializers
from utils.custom_relational_fields import UserNameRelationalField
from django.contrib.auth import get_user_model
from users.api.v1.serializers import UserRetrieveSerializer

from term.models import (
    Term as TermModel ,
    Session as SessionModel,
)

class SessionSerializer(serializers.ModelSerializer):
    # replies = serializers.SerializerMethodField()
    # user = UserEmailNameRelationalField(read_only=True)
    # user = serializers.SlugRelatedField(read_only=True,slug_field='email')
    # student = UserRetrieveSerializer()

    class Meta:
        model = SessionModel
        fields = ["id","type","name","description","location","term" ]



class TermListSerializer(serializers.ModelSerializer):
    # Session = serializers.SerializerMethodField()
    # cracreator = serializers.SerializerMethodField(read_only=True)
    sessions = SessionSerializer(many=True)
    class Meta:
        model = TermModel
        # exclude = ['feed', 'reshare']
        fields = ['id','active', 'type', 'name', 'description',
                  'count','sessions', 'end_at', 'maker']




class TermCreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermModel
        # exclude = ['feed', 'reshare']
        fields = [  'name', 'description', 'pay']





