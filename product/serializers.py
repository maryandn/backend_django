from rest_framework import serializers

from .models import BrandModel, ColorModel, ProductModel


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ['name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ['name']


# class ImgSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImgModel
#         fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(required=True)
    color = ColorSerializer(required=True)

    # img = ImgSerializer(required=True)

    class Meta:
        model = ProductModel
        fields = ('name', 'code', 'price', 'quantity', 'brand', 'color')

    def create(self, validated_data):
        color = validated_data.pop('color')
        brand = validated_data.pop('brand')

        product = ProductModel(**validated_data)

        product.save()
        ProductModel.objects.create(product=product, **brand, **color)

        return product
