# Generated by Django 4.2.5 on 2023-09-27 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productvariant_variant_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariantTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='RequestExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=255)),
                ('option', models.CharField(blank=True, max_length=255, null=True)),
                ('field_type', models.CharField(choices=[('TEXT', 'Text'), ('IMAGE', 'Image'), ('RADIO', 'Radio'), ('SELECT', 'Select')], default='TEXT')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]