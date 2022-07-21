from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework import generics

from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserListSerializer

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            request.user.auth_token.delete()
            return Response(status=200)
        except:
            return Response(status=400)
class GetAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer
    # permission_classes = [IsAuthenticated]


class UserCreateAPIView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer









