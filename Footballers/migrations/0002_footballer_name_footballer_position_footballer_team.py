# Generated by Django 4.2.5 on 2023-09-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Footballers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballer',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='footballer',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='footballer',
            name='team',
            field=models.CharField(default='', max_length=100),
        ),
    ]
