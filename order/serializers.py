from rest_framework import serializers

from order.models import OrderModel, CartModel
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartModel
        fields = ('id_user', 'quantity', 'id_product')
        extra_kwargs = {
            "id_user": {"write_only": True}
        }


class CartProductSerializer(serializers.ModelSerializer):
    id_product = ProductSerializer()

    class Meta:
        model = CartModel
        fields = ['quantity', 'id_product']
        extra_kwargs = {"id_product": {"read_only": True}}


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
