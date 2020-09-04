from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=13, blank=False,
                             validators=[
                                 RegexValidator('^([+])(\d{1,12})$',
                                                'phone incorrect')
                             ]
                             )
