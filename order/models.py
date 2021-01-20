from django.db import models
from user_profile.models import UserModel
from product.models import ProductModel


class CartModel(models.Model):
    class Meta:
        db_table = 'cart'

    id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    id_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class OrderModel(models.Model):
    class Meta:
        db_table = 'order'

    id_user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    date_create = models.DateField(auto_now=True)
