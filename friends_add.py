# -*- coding: utf-8 -*-
from datetime import datetime
import time
import vk

next_date = '30.08.2018'
next_time = '19' + 
next_place = 'в гриль-бар Колбас-Барабас'
next_place = 'в ресторан Максимиланс'

text = '''
Привет&#128075; Лига Индиго собирает под одной крышей умных, талантливых и веселых людей.
Лига Индиго - это не просто очередной квиз&#9757; Раунды ligaindigo.ru/raunds настолько разнообразны, что каждый игрок в команде сможет проявить себя.
Мы уже провели несколько игр, и это было круто&#128293; Фотоотчеты ты можешь посмотреть в нашей группе vk.com/li_tyumen.
'''

if datetime.now() > next_date:
    text = text + 'Следующая игра не за горами, не пропусти;)'
else:
    text = text + 'Приходи на следующую игру' + next_place + 'и блесни логикой, эрудицией, интуицией и чувством юмора;)'


text = '''
Привет&#128075; Лига Индиго собирает под одной крышей умных, талантливых и веселых людей.
Лига Индиго - это не просто очередной квиз&#9757; Раунды ligaindigo.ru/raunds настолько разнообразны, что каждый игрок в команде сможет проявить себя.
Мы уже провели несколько игр, и это было круто&#128293; Фотоотчеты есть в нашей группе vk.com/li_tyumen.
Приходи на следующую игру 2 Августа в 19:08 в гриль-бар Колбас-Барабас и блесни логикой, эрудицией, интуицией и чувством юмора;)
'''

text = '''
Привет&#128075; Лига Индиго собирает под одной крышей умных, талантливых и веселых людей.
Лига Индиго - это не просто очередной квиз&#9757; Раунды ligaindigo.ru/raunds настолько разнообразны, что каждый игрок в команде сможет проявить себя.
Мы уже провели несколько игр, и это было круто&#128293; Фотоотчеты есть в нашей группе vk.com/li_tyumen.
Приходи на следующую игру 16 Августа в 19:08 в ресторан Максимиланс и блесни логикой, эрудицией, интуицией и чувством юмора;)
'''

group_id = 'ESLPodcast72'
group_id = 'mozgoboj_tmn'
group_id = 'quizplease_tmn'
group_id = 'quizium_tmn'
group_id = 'komnatatyumen'

users = vk.users_from_csv(group_id,6786949)

mode = 'w'
file_name = datetime.now().strftime("%Y%m%d_%H%M%S")
for user in users:
    csv_rows = []
    csv_row = {}
    csv_row['dt'] = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    csv_row.update(user)

    r = vk.friends_add(user['id'],text)
    if 'response' in r:
        csv_row['response'] = r['response']
    if 'error' in r:
        csv_row.update(r['error'])

    print(csv_row)
    csv_rows.append(csv_row)
    vk.to_csv(csv_rows, file_name, mode)
    mode = 'a'    

    if 'error' in r:
        if 'captcha_sid' in r['error']:
            break

    #если уже 23, то ждем 8 часов
    #на pythonanywhere время по гринвичу, поэтому -5 часов
    if datetime.now().hour == 23 - 5:
        time.sleep(60*60*8)
    #иначе обычный дилэй в 20 минут
    else:
        time.sleep(60*20)