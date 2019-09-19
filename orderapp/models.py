from django.db import models

# Create your models here.

#抽象表
from mainapp.models import FruitEntity, UserEntity


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间',
                                       auto_now_add=True)

    last_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True)

    class Meta:
        abstract = True

class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~models.Q(pay_status=5))


class OrderModel(BaseModel):
    num = models.CharField(max_length=20,
                           primary_key=True,
                           verbose_name='订单号')

    title = models.CharField(max_length=100,
                           verbose_name='订单名称')

    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                             verbose_name='订单金额')

    pay_type = models.IntegerField(choices=((0, '余额'),
                                            (1, '银行卡'),
                                            (2, '支付宝'),
                                            (3, '微信')),
                                   verbose_name='支付方式',
                                   default=0)

    pay_status = models.IntegerField(choices=((0, '待支付'),
                                            (1, '已支付'),
                                            (2, '带收货'),
                                            (3, '已收货'),
                                            (4, '完成'),
                                            (5, '取消')),
                                   verbose_name='订单状态',
                                     default=0)

    receiver = models.CharField(verbose_name='收货人',
                                max_length=20)

    receiver_phone = models.CharField(max_length=11,
                                      verbose_name='收货人电话')

    receiver_address = models.TextField(verbose_name='收货人地址')

    objects = OrderManager

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_order'
        verbose_name = '订单表'
        verbose_name_plural = verbose_name



#收货地址表
class AddressEntity(BaseModel):
    class Meta:
        db_table = 't_address'
        verbose_name_plural = verbose_name = '收货地址表'

    name = models.CharField(max_length=20,
                            verbose_name='用户姓名')

    phone = models.CharField(max_length=11,
                            verbose_name='用户电话')

    address = models.CharField(max_length=200,
                             verbose_name='用户地址')

    def __str__(self):
        return str(self.name)

#订单表
class OrderModels(BaseModel):
    num = models.CharField(max_length=20,
                           primary_key=True,
                           verbose_name='订单号')

    title = models.CharField(max_length=100,
                             verbose_name='订单名称')

    user_id = models.OneToOneField(UserEntity,
                                   on_delete=models.CASCADE,
                                   verbose_name='用户id')

    address_id = models.OneToOneField(AddressEntity,
                                      on_delete=models.CASCADE,
                                      verbose_name='地址id')


    class Meta:
        db_table = 't_order1'
        verbose_name_plural = verbose_name = '订单管理表'

    def __str__(self):
        return self.num

#订单详情表
class OrderProfile(BaseModel):
    class Meta:
        db_table = 't_orderprofile'
        verbose_name_plural = verbose_name = '订单详情表'

    num = models.OneToOneField(OrderModels,
                               on_delete=models.CASCADE,
                               verbose_name='订单号')

    goods_id = models.ForeignKey(FruitEntity,
                                    on_delete=models.CASCADE,
                                    verbose_name='商品id')

    cnt = models.IntegerField(default=1,
                              verbose_name='数量')

    def __str__(self):
        return str(self.num)

    @property
    def price(self):
        return str(self.cnt * self.goods_id.price)

    @property
    def fruit_info(self):
        return self.goods_id.name+str(self.goods_id.price)+self.goods_id.source

    @property
    def user_info(self):
        return self.num.user_id.name

    @property
    def address_info(self):
        return self.num.address_id.phone+self.num.address_id.address

#收藏表
class ShouCangEntity(models.Model):

    user_id = models.ForeignKey(UserEntity,
                                verbose_name='用户id',
                                max_length=20,
                                on_delete=models.CASCADE)

    goods_id = models.ForeignKey(FruitEntity,
                                 verbose_name='水果id',
                                 max_length=20,
                                 on_delete=models.CASCADE)

    class Meta:
        db_table = 't_shoucang'
        verbose_name_plural = verbose_name = '收藏表'


