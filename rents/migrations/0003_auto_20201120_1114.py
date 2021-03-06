# Generated by Django 3.0.3 on 2020-11-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0002_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingmodel',
            name='product',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ratingmodel',
            name='user',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ratingmodel',
            name='rating',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
