from datetime import datetime
import time
import vk

user_id = 5879128
user_id = 480707139

friends = vk.friends_get(user_id)
for friend in friends:
    #print(friend)
    if 'bdate' not in friend:
        continue
    bdate = friend['bdate'].split('.')
    #if not(datetime.today().month == int(bdate[1]) and datetime.today().day == int(bdate[0])):
    #    continue
    #print(bdate)        
    if friend['id'] == 5879128:
        message = '''
        TEST
        '''
        attachment = 'album' + str(user_id) + '_' + '254187861'
        vk.messages_send(friend['id'],message,attachment)