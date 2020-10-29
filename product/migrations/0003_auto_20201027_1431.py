# Generated by Django 3.1.1 on 2020-10-27 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('product', '0002_auto_20201027_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='brand',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.brandmodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='color',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.colormodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='sub_category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.subproductcategoriesmodels'),
        ),
    ]