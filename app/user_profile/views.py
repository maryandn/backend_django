from rest_framework.generics import CreateAPIView
from .serializers import ProfileSerializer
from .models import Profile


class ProfileView(CreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
