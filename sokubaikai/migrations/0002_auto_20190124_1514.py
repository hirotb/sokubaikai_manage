# Generated by Django 2.1.4 on 2019-01-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sokubaikai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doujinmarketsm',
            name='market_start_time',
            field=models.DateTimeField(),
        ),
    ]