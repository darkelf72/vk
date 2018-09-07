import vk

users = vk.from_csv('quizplease_tmn','csv')
for user in users:
	print(user['id'])