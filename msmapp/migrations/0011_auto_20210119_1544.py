# Generated by Django 3.1.1 on 2021-01-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msmapp', '0010_auto_20210119_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='price',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(max_length=100),
        ),
    ]
