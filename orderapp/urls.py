from django.conf.urls import url
from django.urls import path, re_path

from orderapp.views import order_list, cancle_order, serach, query, shoucang, cart

app_name = 'orderapp'

urlpatterns = [

    path('list/<city_code>/<order_num>', order_list, name='list'),
    path('cancel/<uuid:order_num>', cancle_order, name='cancel'),
    re_path(r'^search/(?P<phone>1[3-57-9][\d]{9})$', serach, name='search'),
    path('query',query, name='query'),
    path('shoucang',shoucang),
    path('cart',cart),



    # url(r'^list2/(?P<city_code>\w+)/(?P<order_num>\d+)$', order_list)

]
