from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from .serializers import UserSerializer, PermissionUserSerializer
from rest_framework.response import Response


class SignInView(CreateAPIView, ListModelMixin):
    serializer_class = UserSerializer


class PermissionUserView(APIView, ListModelMixin):
    serializer_class = PermissionUserSerializer

    def get_authenticate_header(self, request):
        user = PermissionUserSerializer(request.user).data
        return Response(user)
