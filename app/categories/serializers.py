from rest_framework import serializers
from .models import ProductCategoriesModels, SubProductCategoriesModels


class ProductCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoriesModels
        fields = '__all__'


class SubProductCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProductCategoriesModels
        fields = '__all__'
        extra_kwargs = {'categories': {'read_only': True}}
