# Generated by Django 4.2.5 on 2023-10-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='english_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
