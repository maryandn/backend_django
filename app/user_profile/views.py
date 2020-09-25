from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from .serializers import UserSerializer, PermissionUserSerializer
from rest_framework.response import Response


class SignUpView(CreateAPIView):
    serializer_class = UserSerializer


class PermissionUserView(APIView):
    serializer_class = PermissionUserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        data = UserSerializer(user).data
        return Response(data)
