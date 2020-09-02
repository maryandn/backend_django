from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, unique=True, blank=False,
                             validators=[
                                 RegexValidator('^([+])(\d{1,12})$',
                                                'phone incorrect')
                             ]
                             )

    def __str__(self):
        return self.phone
