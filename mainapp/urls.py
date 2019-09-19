from django.urls import path
from mainapp.views import user_list, user_list2, user_list3, add_user, find_fruit, find_store, user_zhuce, user_login, \
    user_logout
from mainapp.views import update_user, delete_user

urlpatterns = [
    path('list', user_list3),
    path('add', add_user),
    path('update', update_user),
    path('del', delete_user),
    path('find', find_store),
    path('zhuce', user_zhuce),
    path('login/', user_login),
    path('logout', user_logout)

]
