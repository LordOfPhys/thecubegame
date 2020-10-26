from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)
    room_status = models.CharField(max_length=5, default='0') 
    user_one = models.ForeignKey(User, related_name='user_one', on_delete='default')
    user_two = models.ForeignKey(User, related_name='user_two', on_delete='default')
    arr_one = models.CharField(max_length=10000, default='0')
    arr_two = models.CharField(max_length=10000, default='0')

    def get_room_status(self):
        return self.room_status
    
    def set_room_status(self, room_status):
        self.room_status = room_status
        self.save()

    def set_arr_one(self, arr_one):
        self.arr_one = arr_one
        self.save()

    def get_arr_one(self):
        return self.arr_one

    def set_arr_two(self, arr_two):
        self.arr_two = arr_two
        self.save()

    def get_arr_two(self):
        return self.arr_two

    def set_user_one(self, user_one):
        self.user_one = user_one
        self.save()

    def get_user_one(self):
        return self.user_one

    def set_user_two(self, user_two):
        self.user_two = user_two
        self.save()

    def get_user_two(self):
        return self.user_two

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name='user', related_name='user', on_delete=models.CASCADE, default='')
    room = models.ForeignKey(Room, related_name='room', on_delete='default')
    x_max = models.CharField(max_length=10, default='0')
    y_max = models.CharField(max_length=10, default='0')
    status = models.CharField(max_length=10, default='0')
    step = models.CharField(max_length=10, default='0')

    def get_user(self):
        return self.user

    def get_step(self):
        return self.step

    def set_step(self, step):
        self.step = step
        self.save()

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        self.save()

    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room
        self.save()

    def get_x_max(self):
        return self.x_max

    def set_x_max(self, x_max):
        self.x_max = x_max
        self.save()

    def get_y_max(self):
        return self.y_max

    def set_y_max(self, y_max):
        self.y_max = y_max
        self.save()


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete='default')
    message = models.TextField()
    def get_Text(self):
        return self.message

