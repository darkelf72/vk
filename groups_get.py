import vk

group = 'quizplease_tmn'
vk.users_to_csv(vk.groups_get(group),group)