from rest_framework import serializers

from .models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('sub_category', 'name', 'code', 'price', 'quantity', 'brand', 'color')

    def create(self, validated_data):
        product = ProductModel(**validated_data)
        product.save()

        return product
