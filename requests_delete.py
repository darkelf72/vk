import time
import vk

user_id = 480707139 #li_in_tyumen
items = vk.friends_get_requests(user_id)
for item in items:
    vk.friends_delete(item)
    time.sleep(0.4)