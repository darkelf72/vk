import vk
log_name = '1'
last_user_id = float(vk.from_csv(log_name,'log')[-1]['id'])
print(last_user_id)