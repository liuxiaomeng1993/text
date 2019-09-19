import json
import re

from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from mainapp.models import CartEntity, FtuitCartEntity, FruitEntity, UserEntity
from orderapp.models import ShouCangEntity

# Create your views here.
from django.urls import reverse


def order_list(request, order_num, city_code):

    msg = order_num + '-' +  city_code

    return render(request, 'order/list_order.html', locals())

def cancle_order(request, order_num):

    msg = order_num

    return render(request, 'order/list_order.html', locals())

def serach(request, phone):

    msg = phone

    return render(request, 'order/list_order.html', locals())

def query(request):
    url = reverse('order:list', args=(20, 30))
    # return HttpResponse('hi,query %s' %  url)
    return redirect(url)

@csrf_exempt
def shoucang(request):
    shoucang_list = []

    user = request.session.get('login_user')
    if not user:
        msg = '请先登陆<a href="http://127.0.0.1:8000/user/login">登陆</a>'
    else:
        global user_id
        user_id = user['user_id']
        users = ShouCangEntity.objects.filter(user_id=user_id).all()
        if len(list(users)) > 0:
            user = [user for user in users]
            for i in user:
                shoucang_list.append(i.goods_id.name)

        else:
            msg = '什么都没有，快去收藏吧'
            user = ''


    info = request.body.decode()
    if info:
        info = json.loads(info)['name']


        if info[0] == '删除':

            fr = FruitEntity.objects.filter(name=info[1]).first()
            sc = ShouCangEntity.objects.filter(goods_id=fr.id).first()
            sc_del = ShouCangEntity.objects.filter(id=sc.id).first()
            sc_del.delete()
            return JsonResponse({'data': '删除成功'})

        else:
            if info[0] in shoucang_list:
                return JsonResponse({'data': '您收藏的商品已存在'})
            else:
                fruits = FruitEntity.objects.filter(name=info[0]).first()


                goods_id = fruits.id

                u = UserEntity.objects.get(id=user_id)
                f = FruitEntity.objects.get(id=goods_id)
                sc_add = ShouCangEntity(user_id=u, goods_id=f)
                sc_add.save()

                return JsonResponse({'data': '添加成功'})

    return render (request, 'shoucang.html', locals())

@csrf_exempt
def cart(request):
    cart_list = []
    user = request.session.get('login_user')
    if not user:
        msg = '请先登陆<a href="http://127.0.0.1:8000/user/login">登陆</a>'
    else:
        global user_id
        user_id = user['user_id']
        carts = CartEntity.objects.filter(user_id=user_id).all()
        l = re.search(r'\d+', str(carts)).span()
        cart_id = str(carts)[l[0]:l[1]]
        if len(list(carts)) > 0:
            fruits = FtuitCartEntity.objects.filter(cart=cart_id).all()
            if len(list(fruits)) > 0:
                f = [f for f in fruits]
                for i in f:
                    cart_list.append(i.fruit.name)
            else:
                msg = '你的购物车空空如也，快去选购吧'
                f = ''
        else:
            msg = '你的购物车空空如也，快去选购吧'
            f = ''

    info = request.body.decode()

    if info:
        info = json.loads(info)['name']

        if info[0] == '删除':
            f_id = FruitEntity.objects.filter(name=info[1]).first()
            no = CartEntity.objects.filter(user_id=user_id).first()
            f_fs = FtuitCartEntity.objects.filter(fruit_id=f_id, cart=no.no).first()
            fce = FtuitCartEntity.objects.filter(id=f_fs.id).first()
            fce.delete()
            return JsonResponse({'data': '删除成功'})

        else:

            if info[0] in cart_list:
                return JsonResponse({'data': '您收藏的商品已存在'})
            else:

                user = CartEntity.objects.filter(user_id=user_id).first()
                f_id = FruitEntity.objects.filter(name=info[0]).first()

                if user:

                    c = CartEntity.objects.get(no=user.no)
                    f = FruitEntity.objects.get(id=f_id.id)
                    tfc_add = FtuitCartEntity(cart=c, fruit=f, cnt=1)
                    tfc_add.save()
                else:
                    no = CartEntity.objects.aggregate(Max('no'))['no__max']
                    no = str(int(no)+1)
                    car = CartEntity(user_id=user_id, no=no)
                    car.save()
                    c = CartEntity.objects.get(no=no)
                    f = FruitEntity.objects.get(id=f_id.id)
                    tfc_add = FtuitCartEntity(cart=c, fruit=f, cnt=1)
                    tfc_add.save()


                return JsonResponse({'data': '添加成功'})
    return render(request, 'cart.html', locals())


