from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserSerializer, PermissionUserSerializer
from rest_framework.response import Response
from rest_framework import status


class SignUpView(CreateAPIView):
    serializer_class = UserSerializer


class PermissionUserView(APIView):
    serializer_class = PermissionUserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        print(user)
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)
