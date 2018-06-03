from datetime import datetime
import time
import vk

user_id = 480707139

items = vk.friends_get_requests(user_id)
now = datetime.now()
file_name = 'requests_del_' + now.strftime("%Y%m%d_%H%M%S")
vk.items_to_csv(items,file_name)

for item in items:
    vk.friends_delete(item)
    time.sleep(0.4)

#vk.friends_delete(20423015)