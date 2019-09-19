import re
import uuid

from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def update(self, **kwargs):
        password = kwargs.get('passwd', None)
        if password and len(password) < 50:
            kwargs['passwd'] = make_password(password)
        super().update(**kwargs)

class UserValidator():
    @classmethod
    def valid_phone(cls, value):
        if not re.match(r'1[3-57-9]\d{9}', value):
            raise ValidationError('手机号码不正确')
        return True

# 客户的用户表
class UserEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='账号')
    age = models.IntegerField(default=0,
                              verbose_name='年龄')
    phone = models.CharField(max_length=11,
                             validators=[UserValidator.valid_phone],
                             verbose_name='手机号',
                             blank=True, # 站点的表单字段值可以为空
                             null=True)  # 数据表的字段可以是null值

    passwd = models.CharField(max_length=100,
                              verbose_name='密码'
                              )

    objects = UserManager()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.passwd) < 50:
            self.passwd = make_password(self.passwd)
        super().save()


    def __str__(self):
        return self.name

    class Meta:
        # 设置表名
        db_table = 'app_user'
        verbose_name = '客户管理'
        # 设置复数的表示方式
        verbose_name_plural = verbose_name

# 水果分类模型
class CateTypeEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='分类名')
    order_num = models.IntegerField(verbose_name='排序')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        ordering = ['-order_num']  # 指定排序字段， - 表示降序
        verbose_name = '水果分类'
        verbose_name_plural = verbose_name


class FruitEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='水果名')
    price = models.FloatField(verbose_name='价格')
    source = models.CharField(max_length=30,
                              verbose_name='源产地')

    category = models.ForeignKey(CateTypeEntity,
                                 on_delete=models.CASCADE )

    name_photo = models.ImageField(verbose_name='photo',
                             upload_to='imags',
                             width_field='photo_width',
                             height_field='photo_height',
                             null=True,
                             blank=True)

    photo_width = models.IntegerField(verbose_name='photo宽',
                                     null=True)

    photo_height = models.IntegerField(verbose_name='photo高',
                                      null=True)

    users = models.ManyToManyField(UserEntity,
                                   db_table='t_collect',
                                   related_name='fruits',
                                   verbose_name='收藏用户列表')

    tags = models.ManyToManyField('TagEntity',
                                  db_table='t_fruit_tags',
                                  related_name='fruits',
                                  verbose_name='所有标签')

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id:  #判断是否为新增
            super().save()


    class Meta:
        db_table = 't_fruit'
        verbose_name = '水果表'
        verbose_name_plural = verbose_name

class StoreEntity(models.Model):
    #默认情况下，模型自动创建主键id字段--隐式
    #但是也可以显示的方式声明主键（primary key)
    id = models.UUIDField(primary_key=True,
                          verbose_name='店号',
                          )

    name = models.CharField(max_length=50,
                            verbose_name='水果商店名')

    store_type = models.CharField(max_length=10,
                                  choices=(('1', '自营'), ('2', '第三方')),
                                  verbose_name='类型',
                                  db_column='type_')

    boss_name = models.CharField(max_length=20,
                                 verbose_name='负责人')

    phone = models.CharField(max_length=11,
                                verbose_name='电话')

    address = models.CharField(max_length=100,
                               verbose_name='商店地址')

    city = models.CharField(max_length=20,
                            verbose_name='所在城市',
                            db_index=True)

    logo = models.ImageField(verbose_name='LOGO',
                             upload_to='store',
                             width_field='logo_width',
                             height_field='logo_height',
                             null=True,
                             blank=True)

    logo_width = models.IntegerField(verbose_name='LOGO宽',
                                     null=True)

    logo_height = models.IntegerField(verbose_name='LOGO高',
                                     null=True)

    summary = models.TextField(verbose_name='介绍',
                               blank=True,
                               null=True)

    opened = models.BooleanField(verbose_name='是否开业',
                                 default=False)

    lat = models.FloatField(max_length=20,
                            verbose_name='纬度',
                            )

    lon = models.FloatField(max_length=20,
                            verbose_name='经度',
                            )

    create_time = models.DateField(verbose_name='成立时间',
                                   auto_now_add=True)

    last_time = models.DateField(verbose_name='最后变更时间',
                                 auto_now=True)

    @property
    def open_time(self):
        print(self.create_time)
        return self.create_time

    def __str__(self):   #站点显示对象的字符串信息
        return self.name+'-'+self.city

    #调用模型保存方法时调用
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:  #判断是否为新增
            self.id = uuid.uuid4().hex
        super().save()

    @property
    def id_(self):
        # return str(self.id).replace('-', '')
        return self.id.hex

    class Meta:  #元数据
        db_table = 't_store'
        unique_together = (('name', 'city'), )
        verbose_name = '水果店'
        verbose_name_plural = verbose_name

class RealProfile(models.Model):
    #声明一对一的关联关系
    user = models.OneToOneField(UserEntity,
                                verbose_name='登陆账号',
                                on_delete=models.CASCADE)

    real_name = models.CharField(max_length=20,
                                 verbose_name='真实姓名')

    real_type = models.CharField(max_length=10,
                                choices=(('0', '身份证'),
                                        ('1', '护照'),
                                        ('2', '驾驶证')))


    number = models.CharField(max_length=30,
                              verbose_name='证件号')

    image1 = models.ImageField(verbose_name='正面照',
                               upload_to='user/real')

    image2 = models.ImageField(verbose_name='反面照',
                               upload_to='user/real'
                               )

    def __str__(self):
        return str(self.user)


    class Meta:
        db_table = 't_profile'
        verbose_name = verbose_name_plural ='实名认证表'


class CartEntity(models.Model):
    class Meta:
        db_table = 't_cart'
        verbose_name_plural = verbose_name = '购物车表'

    user = models.OneToOneField(UserEntity,
                                verbose_name='账号',
                                on_delete=models.CASCADE)

    no = models.CharField(primary_key=True,
                          verbose_name='购物车编号',
                          max_length=5)

    def __str__(self):
        return self.no

class TagEntity(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='标签名')

    order_num = models.IntegerField(default=1,
                                    verbose_name='序号')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = verbose_name = '标签表'

class FtuitCartEntity(models.Model):
    cart = models.ForeignKey(CartEntity,
                             on_delete=models.CASCADE,
                             verbose_name='购物车编号')

    fruit = models.ForeignKey(FruitEntity,
                              on_delete=models.CASCADE,
                              verbose_name='水果')

    cnt = models.IntegerField(verbose_name='数量',
                              default=1)



    def __str__(self):
        return self.fruit.name + ':' + self.no

    @property
    def price(self):
        return round(self.cnt * self.fruit.price, 2)

    class Meta:
        db_table = 't_fruit_cart'
        verbose_name_plural = verbose_name = '购物车详情表'