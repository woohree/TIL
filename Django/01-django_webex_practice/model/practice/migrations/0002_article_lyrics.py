# Generated by Django 3.2.12 on 2022-03-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='lyrics',
            field=models.TextField(default=''),
        ),
    ]
