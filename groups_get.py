from datetime import datetime
import vk

group = 'ESLPodcast72'
group = 'mzgb_tmn'
group = 'quizplease_tmn'
group = 'quizium_tmn'
group = 'komnatatyumen'
user_id = 480707139 #li_in_tyumen

csv_rows = []
users = vk.groups_get(group,user_id)
for user in users:
    if 'deactivated' in user:
        continue
    if 'last_seen' in user:
        last_seen = datetime.fromtimestamp(user['last_seen']['time'])
        if last_seen.year < datetime.today().year:
            continue
    if 'city' in user:
        if user['city']['title'] != 'Тюмень':
            continue
    csv_row = {}
    csv_row['id'] = user['id']
    csv_row['name'] = user['last_name'] + ' ' + user['first_name']
    csv_row['domain'] = user['domain']
    csv_rows.append(csv_row)
if len(csv_rows) > 0:
	vk.to_csv(csv_rows,group,'w')