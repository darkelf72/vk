# -*- coding: utf-8 -*-
from datetime import datetime
import time
import vk

user_id = 5879128
user_id = 480707139

message = '''
Привет&#128075;
Лига Индиго от всего сердца поздравляет тебя с днем рождения&#127874;
И дарит скидку 25% на участие в ближайшей игре для тебя и твоей команды&#128522;
Просто подай заявку в группе https://vk.com/li_tyumen, приходи на игру и покажи это сообщение&#128241;
'''

while 1 == 1:
    print(datetime.now())
    if datetime.now().hour == 10:  
        friends = vk.friends_get(user_id)
        for friend in friends:
            if 'bdate' not in friend:
                continue
            bdate = friend['bdate'].split('.')
            if datetime.today().month == int(bdate[1]) and datetime.today().day == int(bdate[0]):       
            #if friend['id'] == 5879128:
                attachment = 'photo' + str(user_id) + '_' + '456239022'
                vk.messages_send(friend['id'],message,attachment)
                print(friend)
                time.sleep(0.4)
    time.sleep(3600)