from datetime import datetime
import time
import vk

owner_id = 124597198 #mzgb_tmn
owner_id = 155184737 #quizplease_tmn
owner_id = 141854271 #quizium_tmn
exclude_id = []
exclude_id.append(owner_id)
exclude_id.append(376951514) #mozgobojtmn, Анна Ветрова
exclude_id.append(3991928) #id3991928, Антон Сковороднев
exclude_id.append(5947289) #germanoff, Дима Германов

query = 'Регистрация'
keyword = 'чел'
keyword = ''
csv_rows = []

#posts = vk.wall_search(owner_id,query)
posts = vk.wall_get(owner_id)
for post in posts:
    response = vk.wall_get_comments(owner_id,post['id'])
    time.sleep(0.4)
    #response = vk.wall_get_comments(owner_id,3548)
    comments = response['items']
    profiles = response['profiles']
    for comment in comments:
        if abs(comment['from_id']) in exclude_id:
            continue
        if keyword != '' and keyword not in (comment['text']):
            continue

        for profile in profiles:
            if profile['id'] == comment['from_id']:
                break

        csv_row = {}
        csv_row['comment_id'] = comment['id']
        csv_row['dt'] = datetime.fromtimestamp(comment['date']).strftime("%Y/%m/%d %H:%M:%S")
        csv_row['user_id'] = comment['from_id']
        csv_row['name'] = profile['last_name'] + ' ' + profile['first_name']
        if 'screen_name' in profile:
            csv_row['screen_name'] = profile['screen_name']
        else:
            csv_row['screen_name'] = 'deleted'
        csv_row['text'] = comment['text'].replace('\n','')
        print(csv_row)
        csv_rows.append(csv_row)
    #break
vk.to_csv(csv_rows,str(owner_id),'w')

