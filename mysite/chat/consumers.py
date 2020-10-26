# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.models import UserProfile, Room, Message
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        room = Room.objects.get(label=self.room_name)
        up = UserProfile.objects.get(user=self.scope['user'])
        if up.get_room() != room:
            self.close()
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
       # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print(text_data)
        data = json.loads(text_data)
        up = UserProfile.objects.get(user=self.scope['user'])
        room = up.get_room()
        if room.get_user_one() != up.get_user():
            up_enemy = UserProfile.objects.get(user=room.get_user_one())
        else:
            up_enemy = UserProfile.objects.get(user=room.get_user_two())
        if data.get('max_x') is not None and data.get('max_y') is not None:
            up.set_x_max(data['max_x'])
            up.set_y_max(data['max_y'])
            up.set_status('1')
        else:
            if data['ToReturn'] is not None:
                array = data['ToReturn']
                s = '';
                for e in range(len(array) - 1):
                    s += array[e] + " ";
                s += array[len(array) - 1]
                if room.get_user_one() != up.get_user():
                    room.set_arr_two(room.get_arr_two() + " " + s)
                else:
                    room.set_arr_one(room.get_arr_one() + " " + s)
                up.set_status('0')
                up.set_step('0')
                up_enemy.set_step('1')
                up_enemy.set_status('1')
                self.send(text_data=json.dumps({'status_step': up_enemy.get_step(), 'user': str(self.scope['user']), 'r_arr_one': room.get_arr_one(), 'r_arr_two': room.get_arr_two()}))
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'r_arr_two': room.get_arr_two(),
                        'r_arr_one': room.get_arr_one(),
                        'user': str(self.scope['user']),
                        'userTurn': data['ToReturn']
                    }
                )
        

    # Receive message from room group
    def chat_message(self, event):
        message = event['user']
        userTurn = event['userTurn']
        r_arr_two = event['r_arr_two']
        r_arr_one = event['r_arr_one']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'user': message,
            'r_arr_two': r_arr_two,
            'r_arr_one': r_arr_one,
            'userTurn': userTurn
        }))

