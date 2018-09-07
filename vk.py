# -*- coding: utf-8 -*-
import json 
import requests
import time
import csv

import sys
sys.path.append('../')
import mylib

#https://oauth.vk.com/authorize?client_id=6428597&scope=friends,photos,messages,offline,groups&redirect_uri=https://oauth.vk.com/blank.html&display=page&v=5.73&response_type=token
api = 'https://api.vk.com/method/'
access_token = mylib.access_token
v = '5.73'

#Возвращает список идентификаторов друзей пользователя или расширенную информацию о друзьях пользователя
def friends_get(user_id):
    method_name = 'friends.get'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['user_id'] = user_id
    parameters['fields'] = 'sex,domain,nickname,city,last_seen,bdate,online'
    r = requests.get(api + method_name, parameters)
    result = json.loads(r.text)['response']['items']
    print('Friends of', user_id, ':', len(result))
    return result
#friends_get('5879128')

#Возвращает список участников сообщества
def groups_get_members(group_id):
    method_name = 'groups.getMembers'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['group_id'] = group_id
    parameters['count'] = 1000
    parameters['offset'] = 0
    result = []

    while 1 == 1:
        r = requests.get(api + method_name, parameters)
        res = json.loads(r.text)['response']['items']
        result = result + res
        parameters['offset'] = parameters['offset'] + parameters['count']
        if len(res) != parameters['count']:
            break

    print('Members of', group_id, ':', len(result))
    return result
#groups_get_members('mozgoboj_tmn')

#Возвращает расширенную информацию о пользователях
def users_get(user_ids):
    method_name = 'users.get'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['fields'] = 'last_seen,city,domain'
    parameters['user_ids'] = user_ids
    r = requests.get(api + method_name, parameters)
    result = json.loads(r.text)['response'][0]
    print('User ID', user_ids, 'info:\n', result)
    return result
#users_get('mozgobojtmn')

#Возвращает список участников сообщества (с расширенной информацией), которых нет в друзьях у указанного пользователя
def groups_get(group_id,user_id):
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
#print(groups_get('ESLPodcast72'))

#Одобряет или создает заявку на добавление в друзья
def friends_add(user_id, text):
    method_name = 'friends.add'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['user_id'] = user_id
    parameters['text'] = text
    parameters['follow'] = 0
    parameters['captcha_sid'] = 801054743215
    parameters['captcha_key'] = 'hed2k'
    r = requests.get(api + method_name, parameters)
    return json.loads(r.text)

#Возвращает информацию о полученных или отправленных заявках на добавление в друзья для текущего пользователя
def friends_get_requests(user_id):
    method_name = 'friends.getRequests'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['user_id'] = user_id
    #parameters['offset'] = 100
    parameters['count'] = 1000
    parameters['out'] = 1
    r = requests.get(api + method_name, parameters)
    result = json.loads(r.text)['response']['items']
    print('User has', len(result), 'requests')
    return result

#Удаляет пользователя из списка друзей или отклоняет заявку в друзья
def friends_delete(user_id):
    method_name = 'friends.delete'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['user_id'] = user_id
    r = requests.get(api + method_name, parameters)
    result = json.loads(r.text)
    print('User', user_id, result)
    return result

#Отправляет сообщение
def messages_send(user_id,message,attachment):
    method_name = 'messages.send'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['user_id'] = user_id
    parameters['message'] = message
    parameters['attachment'] = attachment
    parameters['captcha_sid'] = 288018680113
    parameters['captcha_key'] = 's4h8c'
    r = requests.get(api + method_name, parameters)
    result = json.loads(r.text)
    print('Message have sent to', user_id, result)
    return result    

#Позволяет приглашать друзей в группу
def groups_invite(group_id,user_id):
    method_name = 'groups.invite'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['group_id'] = group_id
    parameters['user_id'] = user_id
    r = requests.get(api + method_name, parameters)
    result = json.loads(r.text)
    print(user_id, 'was invited to', group_id, result)
    return result   

#Возвращает список записей со стены пользователя или сообщества
def wall_get(owner_id):
    method_name = 'wall.get'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['owner_id'] = -owner_id
    #parameters['filter'] = 'owner'
    parameters['count'] = 100
    parameters['offset'] = 0

    result = []
    while 1 == 1:
        r = requests.get(api + method_name, parameters)
        res = json.loads(r.text)['response']['items']
        result = result + res
        parameters['offset'] = parameters['offset'] + parameters['count']
        if len(res) != parameters['count']:
            break

    print('Wall of', owner_id, 'has', len(result), 'items')
    return result   

#Позволяет искать записи на стене в соответствии с заданными критериями
def wall_search(owner_id,query):
    method_name = 'wall.search'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['owner_id'] = -owner_id
    parameters['query'] = query
    parameters['owners_only'] = 1
    parameters['count'] = 100
    parameters['offset'] = 0

    result = []
    while 1 == 1:
        r = requests.get(api + method_name, parameters)
        res = json.loads(r.text)['response']['items']
        result = result + res
        parameters['offset'] = parameters['offset'] + parameters['count']
        if len(res) != parameters['count']:
            break

    print('Wall of', owner_id, 'has', len(result), 'items with text', query)
    return result   

#Возвращает список комментариев к записи на стене
def wall_get_comments(owner_id,post_id):
    method_name = 'wall.getComments'
    parameters = {}
    parameters['access_token'] = access_token
    parameters['v'] = v
    parameters['owner_id'] = -owner_id
    parameters['post_id'] = post_id
    parameters['count'] = 100
    parameters['offset'] = 0
    parameters['sort'] = 'desc'
    parameters['extended'] = 1
    #parameters['fields'] = ''
    r = requests.get(api + method_name, parameters)
    result = json.loads(r.text)['response']
    print('Post', post_id, 'has', len(result['items']), 'comments')
    return result   

def to_csv(rows, file_name, file_ext='csv', mode='w', encoding='utf-8', delimiter=','):
    f = open(file_name+'.'+file_ext, mode, newline="", encoding=encoding)
    writer = csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter=delimiter)
    if mode == 'w':
        writer.writeheader()
    writer.writerows(rows)
    f.close()
    print('Saved', len(rows), 'rows to file', file_name)

def from_csv(file_name, file_ext='csv', mode='r', encoding='utf-8', delimiter=','):
    f = open(file_name+'.'+file_ext, mode, newline="", encoding=encoding)
    reader = csv.DictReader(f,delimiter=delimiter)
    rows = list(reader)
    f.close()
    print('Loaded', len(rows), 'rows from file', file_name)
    return rows