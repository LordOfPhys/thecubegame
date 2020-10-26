from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from chat.models import Room, Message, UserProfile
import json
import random
from django.http import HttpResponse

@csrf_exempt
def logIn(request):
    if request.method == 'POST':
        a = request.POST['login']
        b = request.POST['password']
        user = authenticate(username=a, password=b)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('../chat')
            else:
                return render(request, 'chat/login.html', {})
        else:
            return render(request, 'chat/login.html', {})
    return render(request, 'chat/login.html', {})

def take_numbers(request):
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    data = {'lenght': a, 'height': b, 'success': True}
    return HttpResponse(json.dumps(data))

def pole(request):
    return render(request, 'chat/pole.html', {})

def index(request):
    return render(request, 'chat/index.html', {})

@csrf_exempt
def room(request, room_name):
    print(request.user)
    if Room.objects.filter(label=room_name).exists() == False:
        # Если комнаты нет - нужно ее создать. При создании оба пользователя - создатель комнаты
        room = Room.objects.get_or_create(label=room_name, user_one = request.user, user_two = request.user)
        room = Room.objects.get(label=room_name)
        if room.get_user_one() == request.user:
            user_arr = room.get_arr_one()
        else:
            user_arr = room.get_arr_two()
        up = UserProfile.objects.get(user = request.user)
        up.set_step('1')
        up.set_room(room)
        return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), 'room_status': mark_safe(json.dumps(room.get_room_status())),
                                              'status_user': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_status())), 
                                              'user': mark_safe(json.dumps(str(request.user))),
                                              'arr_one': mark_safe(json.dumps(room.get_arr_one())),
                                              'arr_two': mark_safe(json.dumps(room.get_arr_two())),
                                              'user_arr': mark_safe(json.dumps(user_arr)),
                                              'user_x_max': mark_safe(json.dumps(up.get_x_max())),
                                              'user_y_max': mark_safe(json.dumps(up.get_y_max())),
                                              'step': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_step()))})
    else:
        # Если комната есть - нужно понять, заполнена ли она (должны быть всего 2 различных человека)
        room = Room.objects.get(label=room_name)
        if room.get_user_one() == request.user:
            user_arr = room.get_arr_one()
        else:
            user_arr = room.get_arr_two()
        if room.get_user_one() == room.get_user_two():
            if request.method == 'POST' and request.user != room.get_user_one():
                up = UserProfile.objects.get(user = request.user)
                old_room = up.get_room()
                up.set_room(room)
                up.set_step('0')
                a = ['00', '09', '90', '99']
                a_a = random.choice(a)
                b = []
                for i in range(len(a)):
                    if a[i] != a_a:
                        b.append(a[i])
                room.set_arr_one(a_a)
                room.set_arr_two(random.choice(b))
                room.set_room_status('1')
                room.set_user_two(request.user)
                if old_room.get_user_one() == old_room.get_user_two():
                    old_room.delete()
                return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), 'room_status': mark_safe(json.dumps(room.get_room_status())),
                                              'status_user': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_status())),
                                              'arr_one': mark_safe(json.dumps(room.get_arr_one())),
                                              'arr_two': mark_safe(json.dumps(room.get_arr_two())),
                                              'user_x_max': mark_safe(json.dumps(up.get_x_max())),
                                              'user_arr': mark_safe(json.dumps(user_arr)),
                                              'user_y_max': mark_safe(json.dumps(up.get_y_max())),
                                              'user': mark_safe(json.dumps(str(request.user))),
                                              'step': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_step()))}) 
            return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), 'room_status': mark_safe(json.dumps(room.get_room_status())),
                                              'status_user': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_status())),
                                              'user': mark_safe(json.dumps(str(request.user))),
                                              'user_x_max': mark_safe(json.dumps(up.get_x_max())),
                                              'user_y_max': mark_safe(json.dumps(up.get_y_max())),
                                              'user_arr': mark_safe(json.dumps(user_arr)),
                                              'arr_one': mark_safe(json.dumps(room.get_arr_one())),
                                              'arr_two': mark_safe(json.dumps(room.get_arr_two())),
                                              'step': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_step()))}) 
        else:
            up = UserProfile.objects.get(user=request.user)
            if up.get_room() != room:
                return HttpResponse('No chin chopa pls')
            else:
                return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), 'room_status': mark_safe(json.dumps(room.get_room_status())),
                                              'status_user': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_status())),
                                              'user': mark_safe(json.dumps(str(request.user))),
                                              'user_x_max': mark_safe(json.dumps(up.get_x_max())),
                                              'user_y_max': mark_safe(json.dumps(up.get_y_max())),
                                              'user_arr': mark_safe(json.dumps(user_arr)),
                                              'arr_one': mark_safe(json.dumps(room.get_arr_one())),
                                              'arr_two': mark_safe(json.dumps(room.get_arr_two())),
                                              'step': mark_safe(json.dumps(UserProfile.objects.get(user = request.user).get_step()))}) 
