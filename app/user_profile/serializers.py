from rest_framework import serializers
from .models import ProfileModel, UserModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('phone',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'profile')

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        ProfileModel.objects.create(user=user, **profile)

        return user


class PermissionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('is_superuser',)
