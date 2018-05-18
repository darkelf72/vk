from datetime import datetime
import time
import vk

user_id = 480707139

friends = vk.friends_get(user_id)
for friend in friends:
	bdate = datetime.fromtimestamp(friend['bdate'])
	#if bdate == datetime.today():
	if friend['id'] == datetime.today():
		message = '''
		TEST
		'''
		attachment = 'doc' + str(user_id) + '_' + 'id media'
		vk.messages_send(friend['id'],message,attachment)