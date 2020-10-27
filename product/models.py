from django.db import models

from categories.models import SubProductCategoriesModels


class BrandModel(models.Model):
    class Meta:
        db_table = 'product_brand'

    name = models.CharField(max_length=20)


class ColorModel(models.Model):
    class Meta:
        db_table = 'product_color'

    name = models.CharField(max_length=20)


# class ImgModel(models.Model):
#     class Meta:
#         db_table = 'product_img'
#
#     product = models.OneToOneField(ProductModel, on_delete=models.CASCADE, related_name='img')
#     img = models.ImageField()


class TitleModel(models.Model):
    class Meta:
        db_table = 'product_title'

    name = models.CharField(max_length=50)


class DescriptionModel(models.Model):
    class Meta:
        db_table = 'product_description'

    name = models.TextField(max_length=500)


class ProductModel(models.Model):
    class Meta:
        db_table = 'product'

    sub_category = models.OneToOneField(SubProductCategoriesModels, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=20)
    code = models.IntegerField(unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    brand = models.OneToOneField(BrandModel, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(ColorModel, on_delete=models.SET_NULL, null=True)
    title = models.OneToOneField(TitleModel, on_delete=models.SET_NULL, null=True)
    description = models.OneToOneField(DescriptionModel, on_delete=models.SET_NULL, null=True)
