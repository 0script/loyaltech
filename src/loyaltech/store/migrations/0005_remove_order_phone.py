# Generated by Django 4.0.3 on 2022-04-05 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_products_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]