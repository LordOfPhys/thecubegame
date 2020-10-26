from django.contrib import admin
from chat.models import Room, Message, UserProfile

admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(Message)
# Register your models here.
