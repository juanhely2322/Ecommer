# Generated by Django 4.0.4 on 2022-06-15 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_alter_category_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
    ]
