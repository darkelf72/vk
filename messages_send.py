# -*- coding: utf-8 -*-
import vk
import csv
import time

user_id = 5879128 #rodionov_sa
user_id = 480707139 #li_in_tyumen

f = open('contacts.txt', "r", newline="", encoding='cp1251')
reader = csv.reader(f,delimiter='\t')

for row in reader:
    print(row)
    message = row[1] + ', "Лига Индиго Тюмень" приветствует команду "' + row[0] + '" '
    message = message + 'и приглашает принять участие в финале первого сезона!' + '\n'
    message = message + 'В игре вас ждут новые раунды, необычные и крутые призы :)' + '\n'
    message = message + 'Игра состоится 06.09 в гриль-баре Колбас-Барабас, начало в 19:09.' + '\n'
    message = message + 'С нетерпением ждём встречи!'

    message = 'Добрый день, ' + row[1] + '! Возможно, сегодня было уже достаточно голосований, но, если несложно, Лига Индиго просит проголосовать еще раз - в выборе дня проведения игр)' + '\n'
    message = message + 'Пост с голосовалкой находится у нас в группе vk.com/li_tyumen?w=wall-148853382_404' + '\n'
    message = message + 'Спасибо :)' 

    message = 'Добрый день, ' + row[1] + '!' + '\n'
    message = message + 'Мы рады представить анонс первой игры осеннего сезона vk.com/li_tyumen?w=wall-148853382_413' + '\n'
    message = message + 'Также хотим напомнить о том, что в Лиге Индиго есть такая штука как "Баттлы" ligaindigo.ru/faq-items/battly/' + '\n'
    message = message + 'Баттл с другой командой - это +100 к азарту и дополнительная мотивация победить). ' + '\n'
    message = message + 'Вызвать команду-соперника на баттл можно прямо в комментариях к анонсу vk.com/li_tyumen?w=wall-148853382_413' + '\n'
    message = message + 'Если возникнет какой-то вопрос - пишите его там же в комментариях.' + '\n'
    message = message + 'Список команд и капитанов уже подавших заявки на игру: ' + '\n'
    message = message + 'Усы Брежнева, vk.com/id347457951' + '\n'
    message = message + 'Убрироманы, vk.com/id2417468' + '\n'
    message = message + 'Сборная разборная, vk.com/id36416239' + '\n'
    message = message + 'Дежурные по апрелю, vk.com/angell_lla' + '\n'
    message = message + 'Гимназисты и религиовед, vk.com/id7043546' + '\n'
    message = message + 'Lady в кедах, vk.com/id275014210' + '\n'
    message = message + 'Хомяк и Ко, vk.com/id16915604' + '\n'
    message = message + 'Без Собаки, vk.com/id1631017' + '\n'
    message = message + 'Аист с герба Гааги, vk.com/id5708539'

    message = 'Привет, ' + row[1] + '!' + '\n'
    message = message + 'Совсем недавно прошла первая игра осеннего сезона и мы будем рады получить от вас фидбэк для того, чтобы сделать новый сезон еще интереснее чем предыдущий.' + '\n'
    message = message + 'Два простых вопроса: что нравится и что не нравится на наших играх?)' + '\n'
    message = message + 'Например: музыка, ведущая, какие-то изменения, которые бы вы хотели увидеть и т.д.?'

    message = row[1] + ', "Лига Индиго Тюмень" приветствует команду "' + row[0] + '" '
    message = message + 'и приглашает принять участие в 3й игре второго сезона!' + '\n'
    message = message + 'vk.com/li_tyumen?w=wall-148853382_485' + '\n'
    message = message + 'Вас ждут 5 умопомрачительных раундов - один из них посвящен Хеллоуину&#127875;' + '\n'
    message = message + 'Игра состоится 01.11 в ресторане Максимилианс, начало в 19:11.' + '\n'
    message = message + 'С нетерпением ждём встречи!'

    attachment = ''
    vk.messages_send(row[3],message,attachment)
    time.sleep(3)
f.close()
