from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer
from .models import UserModel


class UserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
