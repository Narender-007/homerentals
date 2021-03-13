# Generated by Django 3.0.3 on 2020-10-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('user', models.CharField(max_length=60)),
                ('product', models.CharField(max_length=60)),
            ],
        ),
    ]