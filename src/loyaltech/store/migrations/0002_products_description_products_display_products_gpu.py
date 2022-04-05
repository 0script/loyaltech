# Generated by Django 4.0.3 on 2022-04-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default='Short Description About The Product', max_length=50),
        ),
        migrations.AddField(
            model_name='products',
            name='display',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='products',
            name='gpu',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]