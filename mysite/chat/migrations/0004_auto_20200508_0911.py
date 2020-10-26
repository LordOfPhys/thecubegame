# Generated by Django 2.2 on 2020-05-08 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_auto_20200508_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_max', models.CharField(default='0', max_length=10)),
                ('y_max', models.CharField(default='0', max_length=10)),
                ('room', models.ForeignKey(on_delete='default', related_name='room', to='chat.Room')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.RemoveField(
            model_name='gameroom',
            name='user_one',
        ),
        migrations.RemoveField(
            model_name='gameroom',
            name='user_two',
        ),
        migrations.DeleteModel(
            name='GameMessage',
        ),
        migrations.DeleteModel(
            name='GameRoom',
        ),
    ]