# Generated by Django 5.0.4 on 2024-06-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]