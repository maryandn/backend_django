from django.db import models


class ProductCategoriesModels(models.Model):
    class Meta:
        db_table = 'product_categories'

    name = models.CharField(max_length=40, unique=True, )


class SubProductCategoriesModels(models.Model):
    class Meta:
        db_table = 'sub_product_categories'

    categories = models.ForeignKey(ProductCategoriesModels, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=40, unique=True)
