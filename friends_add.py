from datetime import datetime
import time
import vk

text = 'Привет! Лига Индиго открывает регистрацию на первую игру весенней серии! Её проведет спортсменка, комсомолка и просто красавица Полина Асташева! Добавляй нас в друзья, вступай в группу Лига Индиго. Тюмень и следи за новостями!'
text = '''
Привет) Совсем скоро Лига Индиго соберёт под одной крышей много умных и талантливых людей.
Приходи 24 апреля в 19:04 в гриль-бар Колбас-Барабас и блесни логикой, эрудицией, интуицией и чувстовом юмора!
Вступай в группу Лига Индиго. Тюмень и следи за новостями;)
'''

text = '''
Привет) Лига Индиго собирает под одной крышей много умных и талантливых людей.
Мы только что провели первую игру, и это было круто! Совсем скоро будет готов фотоотчет в нашей группе https://vk.com/li_tyumen.
Вторая игра не за горами, не пропусти;)
'''

text = '''
Привет&#128075;
[li_tyumen|Лига Индиго] собирает под одной крышей умных, талантливых и веселых людей.
[li_tyumen|Лига Индиго] - это не просто очередной квиз&#9757; Раунды ligaindigo.ru/raunds настолько разнообразны, что каждый игрок в команде сможет проявить себя.
Мы уже провели первую игру, и это было круто&#128293; Фотоотчет ты можешь посмотреть в нашей группе [li_tyumen|Лига Индиго. Тюмень].
Приходи на следующую игру 10 Мая в 19:05 в гриль-бар Колбас-Барабас и блесни логикой, эрудицией, интуицией и чувством юмора &#127891;&#127942;
[li_tyumen|Cледи за новостями]&#128521;
'''

text = '''
Привет&#128075; Лига Индиго собирает под одной крышей умных, талантливых и веселых людей.
Лига Индиго - это не просто очередной квиз&#9757; Раунды ligaindigo.ru/raunds настолько разнообразны, что каждый игрок в команде сможет проявить себя.
Мы уже провели первую игру, и это было круто&#128293; Фотоотчет ты можешь посмотреть в нашей группе vk.com/li_tyumen.
Приходи на следующую игру 10 Мая в 19:05 в гриль-бар Колбас-Барабас и блесни логикой, эрудицией, интуицией и чувством юмора;)
'''

text = '''
Привет&#128075; Лига Индиго собирает под одной крышей умных, талантливых и веселых людей.
Лига Индиго - это не просто очередной квиз&#9757; Раунды ligaindigo.ru/raunds настолько разнообразны, что каждый игрок в команде сможет проявить себя.
Мы уже провели несколько игр, и это было круто&#128293; Фотоотчеты ты можешь посмотреть в нашей группе vk.com/li_tyumen.
Следующая игра не за горами, не пропусти;)
'''

group_id = 'mozgoboj_tmn'
#group_id = 'ESLPodcast72'
#vk.users_to_csv(vk.groups_get(group_id),group_id)
users = vk.users_from_csv(group_id,27274486)

now = datetime.now()
file_name = now.strftime("%Y%m%d_%H%M%S")
for user in users:
    f = open(file_name+'.log', "a", encoding='utf-8')
    now = datetime.now()
    print(now.strftime("%Y/%m/%d %H:%M:%S"))
    f.write(now.strftime("%Y/%m/%d %H:%M:%S") + ',')
    print(user['id'], user['last_name'], user['first_name'], user['domain'])
    f.write(str(user['id']) + ',' + user['last_name'] + ',' + user['first_name'] + ',' + user['domain'] + ',')
    #text = now.strftime("%d/%m/%y %H:%M")
    response = vk.friends_add(user['id'],text)

    if 'response' in response:
        print('response:', response['response'])
        f.write(str(response['response']) + ',')
    if 'error' in response:
        print('error_code:', response['error']['error_code'])
        print('error_msg:', response['error']['error_msg'])
        f.write('error_code: ' + str(response['error']['error_code']) + ',')
        f.write('error_msg: ' + response['error']['error_msg'] + ',')
        if 'captcha_sid' in response['error']:
            print('captcha_sid:', response['error']['captcha_sid'])
            print('captcha_img:', response['error']['captcha_img'])
            f.write('captcha_sid: ' + str(response['error']['captcha_sid']) + ',')
            f.write('captcha_img: ' + response['error']['captcha_img'] + ',')
        break
    f.write('\n')
    f.close()
    time.sleep(1200)