from rest_framework import serializers

from .models import ProductModel, BrandModel, ColorModel, ImgModel


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ('id', 'name')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ('id', 'name')


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgModel
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    img = ImgSerializer(read_only=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'code', 'price', 'quantity', 'img', 'brand', 'color')

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)


class ProductChangeSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    img = ImgSerializer(read_only=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'code', 'price', 'quantity', 'img', 'brand', 'color')
        extra_kwargs = {"code": {"read_only": True}}
