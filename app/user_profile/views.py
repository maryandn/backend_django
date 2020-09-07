from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from .serializers import UserSerializer
from .models import UserModel
from rest_framework.response import Response


class SignInView(CreateAPIView, ListModelMixin):
    serializer_class = UserSerializer


class UserView(APIView, ListModelMixin):
    serializer_class = UserSerializer

    def get(self, request):
        user = UserSerializer(request.user).data
        return Response(user)
