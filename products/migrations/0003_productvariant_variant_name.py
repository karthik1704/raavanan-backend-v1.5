# Generated by Django 4.2.5 on 2023-09-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='variant_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]