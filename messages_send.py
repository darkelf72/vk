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
    attachment = ''
    vk.messages_send(row[3],message,attachment)
    time.sleep(1)
f.close()
