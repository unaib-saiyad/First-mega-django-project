# Generated by Django 3.2.6 on 2021-09-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20210904_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='avtar',
            field=models.ImageField(default='', upload_to='avtar/'),
        ),
    ]