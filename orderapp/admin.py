from django.contrib import admin

# Register your models here.
from orderapp.models import OrderModel, OrderProfile, AddressEntity, OrderModels, ShouCangEntity


class OrderAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'price', 'pay_type', 'pay_status', 'receiver', 'receiver_phone', 'receiver_address')
    fields = ('num', 'title', 'price', 'pay_type', 'pay_status', 'receiver', 'receiver_phone', 'receiver_address')

class OrderProfileAdmin(admin.ModelAdmin):
    list_display = ('num', 'goods_id', 'cnt', 'price', 'fruit_info_title', 'user_info', 'address_info')
    fields = ('num', 'goods_id', 'cnt')

    def fruit_info_title(self, obj):
        return obj.fruit_info

    fruit_info_title.short_description = '水果详情'

class  AddressEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')

class OrderModelsAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'user_id', 'address_id')

class ShouCangEntityAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'goods_id')

admin.site.register(OrderModel, OrderAdmin)
admin.site.register(OrderProfile, OrderProfileAdmin)
admin.site.register(AddressEntity, AddressEntityAdmin)
admin.site.register(OrderModels, OrderModelsAdmin)
admin.site.register(ShouCangEntity, ShouCangEntityAdmin)