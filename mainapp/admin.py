from django.contrib import admin

from mainapp.models import UserEntity, CateTypeEntity, FruitEntity, StoreEntity, RealProfile, CartEntity, \
    FtuitCartEntity


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # 列表中显示的字段
    list_display = ('id', 'name', 'phone')
    #list_per_page = 2  # 每一页显示记录数
    list_filter = ('id', 'phone')  # 过滤器（一般配置分类字段）
    search_fields = ('id', 'phone')  # 搜索字段

class CateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num')

class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'price', 'category', 'name_photo')
    fields = ('name', 'source', 'price', 'category', 'name_photo')
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id_', 'name', 'store_type', 'boss_name', 'phone', 'address', 'city', 'logo', 'open_time')
    fields = ('name', 'store_type', 'boss_name', 'phone', 'address', 'city', 'lat', 'lon', 'logo', 'summary')
class RealProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'real_name', 'number', 'real_type')

class CartEntityAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'no')


class FtuitCartEntityAdmin(admin.ModelAdmin):
    list_display = ('cart', 'fruit', 'cnt', 'price')
    fields = ('cart', 'fruit', 'cnt')


# 将模型增加到站点中
admin.site.register(UserEntity, UserAdmin)
admin.site.register(CateTypeEntity, CateTypeAdmin)
admin.site.register(FruitEntity, FruitAdmin)
admin.site.register(StoreEntity, StoreAdmin)
admin.site.register(RealProfile, RealProfileAdmin)
admin.site.register(CartEntity, CartEntityAdmin)
admin.site.register(FtuitCartEntity, FtuitCartEntityAdmin)
