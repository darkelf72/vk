from datetime import datetime
import time
import vk

owner_id = 124597198
query = 'Регистрация'
exclude_id = [owner_id,376951514]
csv_rows = []

posts = vk.wall_search(owner_id,query)
for post in posts:
    response = vk.wall_get_comments(owner_id,post['id'])
    time.sleep(0.4)
    #response = vk.wall_get_comments(owner_id,3548)
    comments = response['items']
    profiles = response['profiles']
    for comment in comments:
        if abs(comment['from_id']) in exclude_id:
            continue
        if 'чел' not in (comment['text']):
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

        csv_rows.append(csv_row)
    #break
vk.to_csv(csv_rows,'test')

