import vk

#group = 'quizplease_tmn'
group = 'quizium_tmn'
vk.users_to_csv(vk.groups_get(group),group)