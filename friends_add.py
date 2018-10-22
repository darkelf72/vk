# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import time
import vk

next_date = datetime(2018,11,1)
next_hour = 19
next_minute = next_date.month
next_datetime = next_date + timedelta(hours=next_hour) + timedelta(minutes=next_minute)
next_place = 'гриль-бар Колбас-Барабас'
next_place = 'ресторан Максимилианс'
next_text = next_datetime.strftime("%d %B %H:%M") + ' в ' + next_place

text = '''
Привет&#128075; Лига Индиго собирает под одной крышей умных, талантливых и веселых людей.
Лига Индиго - это не просто очередной квиз&#9757; Раунды ligaindigo.ru/raunds настолько разнообразны, что каждый игрок в команде сможет проявить себя.
Фотоотчеты с наших игр&#128293; ты можешь посмотреть в группе vk.com/li_tyumen.
'''
#на pythonanywhere время по гринвичу, поэтому -5 часов
if datetime.now() > next_datetime - timedelta(hours=5):
    text = text + 'Следующая игра не за горами, не пропусти;)'
else:
    text = text + 'Приходи на следующую игру ' + next_text + ' и блесни логикой, эрудицией, интуицией и чувством юмора;)'

group_id = 'ESLPodcast72'
group_id = 'mozgoboj_tmn'
group_id = 'quizplease_tmn'
group_id = 'quizium_tmn'
group_id = 'komnatatyumen'

#last_user_id = 26495083
#log_name = datetime.now().strftime("%Y%m%d_%H%M%S")

try:
    last_user_id = float(vk.from_csv(group_id,'log')[-1]['id'])
except:
    last_user_id = 0

users = vk.from_csv(group_id)
skipped = 0
mode = 'w'
for user in users:
    if float(user['id']) <= last_user_id:
        skipped += 1
        continue
    if skipped > 0:
        print('Skipped',skipped,'users')
        skipped = 0

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
    vk.to_csv(csv_rows, group_id, 'log', mode)
    mode = 'a'

    if 'error' in r:
        if 'captcha_sid' in r['error']:
            break
            #raise SystemExit

    #если уже 23, то ждем 8 часов
    #если 23, то выходим - задание запустит скрипт в 7:00
    #на pythonanywhere время по гринвичу, поэтому -5 часов
    if datetime.now().hour == 23 - 5:
        time.sleep(60*60*8)
        #raise SystemExit
    #иначе обычный дилэй в 20 минут
    else:
        time.sleep(60*20)