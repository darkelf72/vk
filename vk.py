# -*- coding: utf-8 -*-
import requests
import time
import csv

import sys
sys.path.append('../')
import mylib

#https://oauth.vk.com/authorize?client_id=6428597&scope=friends,photos,messages,offline,groups&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.73&response_type=token

#Выполнить метод api и получить в ответ json
def requests_get(method_name, parameters):
    api = 'https://api.vk.com/method/'
    parameters['access_token'] = mylib.access_token
    parameters['v'] = '5.73'
    r = requests.get(api + method_name, parameters)
    rj = r.json()
    if 'error' in rj:
        print(rj)
        #sys.exit()
    return rj

#Выполнить метод api и получить в ответ json всех элементов
def requests_get_all(method_name, parameters):
    rj_all = []
    while 1 == 1:
        rj = requests_get(method_name, parameters)
        rj = rj['response']['items']
        rj_all = rj_all + rj
        parameters['offset'] = parameters['offset'] + parameters['count']
        if len(rj) != parameters['count']:
            break
    return rj_all

#Возвращает список идентификаторов друзей пользователя или расширенную информацию о друзьях пользователя
def friends_get(user_id):
    method_name = 'friends.get'
    parameters = {}
    parameters['user_id'] = user_id
    parameters['fields'] = 'sex,domain,nickname,city,last_seen,bdate,online'
    rj = requests_get(method_name, parameters)
    rj = rj['response']['items']
    print('Friends of', user_id, ':', len(rj))
    return rj

#Возвращает список участников сообщества
def groups_get_members(group_id):
    method_name = 'groups.getMembers'
    parameters = {}
    parameters['group_id'] = group_id
    parameters['count'] = 1000
    parameters['offset'] = 0
    rj = requests_get_all(method_name, parameters)
    print('Members of', group_id, ':', len(rj))
    return rj

#Возвращает расширенную информацию о пользователях
def users_get(user_ids):
    method_name = 'users.get'
    parameters = {}
    parameters['fields'] = 'last_seen,city,domain'
    parameters['user_ids'] = user_ids
    rj = requests_get(method_name, parameters)
    rj = rj['response'][0]
    print('User ID', user_ids, 'info:\n', rj)
    return rj

#Возвращает список участников сообщества (с расширенной информацией), которых нет в друзьях у указанного пользователя
def groups_get(group_id, user_id):
    users = []
    friends = friends_get(user_id)
    members = groups_get_members(group_id)
    for member in members:
        #если пользователь уже есть в друзьях у указанного пользователя, то не добавляем его в список
        if next((True for friend in friends if friend["id"] == member), False):
            continue
        user = users_get(member)
        users.append(user)
        time.sleep(0.4)
    print('Got info about', len(users), 'users of', group_id)
    return users

#Одобряет или создает заявку на добавление в друзья
def friends_add(user_id, text):
    method_name = 'friends.add'
    parameters = {}
    parameters['user_id'] = user_id
    parameters['text'] = text
    parameters['follow'] = 0
    parameters['captcha_sid'] = 801054743215
    parameters['captcha_key'] = 'hed2k'
    rj = requests_get(method_name, parameters)
    return rj

#Возвращает информацию о полученных или отправленных заявках на добавление в друзья для текущего пользователя
def friends_get_requests(user_id):
    method_name = 'friends.getRequests'
    parameters = {}
    parameters['user_id'] = user_id
    parameters['out'] = 1
    parameters['count'] = 1000
    parameters['offset'] = 0
    rj = requests_get_all(method_name, parameters)
    #rj = rj['response']['items']
    print('User has', len(rj), 'requests')
    return rj

#Удаляет пользователя из списка друзей или отклоняет заявку в друзья
def friends_delete(user_id):
    method_name = 'friends.delete'
    parameters = {}
    parameters['user_id'] = user_id
    rj = requests_get(method_name, parameters)
    print('User', user_id, rj)
    return rj

#Отправляет сообщение
def messages_send(user_id, message, attachment):
    method_name = 'messages.send'
    parameters = {}
    parameters['user_id'] = user_id
    parameters['message'] = message
    parameters['attachment'] = attachment
    parameters['captcha_sid'] = 590442462468
    parameters['captcha_key'] = 'dkq8q'
    rj = requests_get(method_name, parameters)
    print('Message have sent to', user_id, rj)
    return rj    

#Позволяет приглашать друзей в группу
def groups_invite(group_id, user_id):
    method_name = 'groups.invite'
    parameters = {}
    parameters['group_id'] = group_id
    parameters['user_id'] = user_id
    rj = requests_get(method_name, parameters)
    print(user_id, 'was invited to', group_id, rj)
    return rj   

#Возвращает список записей со стены пользователя или сообщества
#Идентификатор сообщества в параметре owner_id необходимо указывать со знаком "-"
def wall_get(owner_id):
    method_name = 'wall.get'
    parameters = {}
    parameters['owner_id'] = owner_id
    #parameters['filter'] = 'owner'
    parameters['count'] = 100
    parameters['offset'] = 0
    rj = requests_get_all(method_name, parameters)
    print('Wall of', owner_id, 'has', len(rj), 'items')
    return rj   

#Позволяет искать записи на стене в соответствии с заданными критериями
def wall_search(owner_id, query):
    method_name = 'wall.search'
    parameters = {}
    parameters['owner_id'] = owner_id
    parameters['query'] = query
    parameters['owners_only'] = 1
    parameters['count'] = 100
    parameters['offset'] = 0
    rj = requests_get_all(method_name, parameters)
    print('Wall of', owner_id, 'has', len(rj), 'items with text', query)
    return rj   

#Возвращает список комментариев к записи на стене
def wall_get_comments(owner_id, post_id):
    method_name = 'wall.getComments'
    parameters = {}
    parameters['owner_id'] = owner_id
    parameters['post_id'] = post_id
    parameters['count'] = 100
    parameters['offset'] = 0
    parameters['sort'] = 'desc'
    parameters['extended'] = 1
    #parameters['fields'] = ''
    rj = requests_get(method_name, parameters)
    rj = rj['response']
    print('Post', post_id, 'has', len(rj['items']), 'comments')
    return rj   

def to_csv(rows, file_name, file_ext='csv', mode='w', encoding='utf-8', delimiter=','):
    f = open(file_name+'.'+file_ext, mode, newline="", encoding=encoding)
    writer = csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter=delimiter)
    if mode == 'w':
        writer.writeheader()
    writer.writerows(rows)
    f.close()
    print('Saved', len(rows), 'rows to file', file_name, file_ext)

def from_csv(file_name, file_ext='csv', mode='r', encoding='utf-8', delimiter=','):
    f = open(file_name+'.'+file_ext, mode, newline="", encoding=encoding)
    reader = csv.DictReader(f,delimiter=delimiter)
    rows = list(reader)
    f.close()
    print('Loaded', len(rows), 'rows from file', file_name, file_ext)
    return rows