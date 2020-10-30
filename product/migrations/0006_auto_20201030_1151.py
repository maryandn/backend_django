# Generated by Django 3.1.2 on 2020-10-30 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201027_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='product/img')),
            ],
            options={
                'db_table': 'product_img',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.imgmodel'),
        ),
    ]
