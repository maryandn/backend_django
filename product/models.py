import os

from django.db import models

from categories.models import SubProductCategoriesModels


class BrandModel(models.Model):
    class Meta:
        db_table = 'product_brand'

    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}.{self.name}'


class ColorModel(models.Model):
    class Meta:
        db_table = 'product_color'

    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}.{self.name}'


class ImgModel(models.Model):
    class Meta:
        db_table = 'product_img'

    name = models.ImageField(upload_to=os.path.join('product', 'img'))


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

    sub_category = models.ForeignKey(SubProductCategoriesModels,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     )

    name = models.CharField(max_length=20)
    code = models.IntegerField(unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    img = models.ForeignKey(ImgModel, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(BrandModel, unique=False, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(ColorModel, unique=False, on_delete=models.SET_NULL, null=True)
    title = models.OneToOneField(TitleModel, unique=False, on_delete=models.SET_NULL, null=True)
    description = models.OneToOneField(DescriptionModel, on_delete=models.SET_NULL, null=True)
