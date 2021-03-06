# Generated by Django 3.2.7 on 2021-11-22 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this category should be treated as active. Unselect this instead of category accounts.', verbose_name='active')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this product should be treated as active. Unselect this instead of product accounts.', verbose_name='active')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productscategory')),
            ],
        ),
    ]
