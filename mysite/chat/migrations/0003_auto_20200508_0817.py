# Generated by Django 2.2 on 2020-05-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_gamemessage_gameroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='mas_user_one',
            field=models.CharField(default='0', max_length=10000),
        ),
        migrations.AddField(
            model_name='gameroom',
            name='mas_user_two',
            field=models.CharField(default='0', max_length=10000),
        ),
        migrations.AddField(
            model_name='gameroom',
            name='status',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
