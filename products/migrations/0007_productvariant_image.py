# Generated by Django 4.2.5 on 2023-09-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_productvariant_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]