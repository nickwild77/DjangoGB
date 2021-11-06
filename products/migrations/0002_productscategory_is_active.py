# Generated by Django 3.2.7 on 2021-11-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productscategory',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this category should be treated as active. Unselect this instead of category accounts.', verbose_name='active'),
        ),
    ]
