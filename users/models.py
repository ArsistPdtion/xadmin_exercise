from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    # define sex selection rule
    GENDER_CHOICES = (
        ('male','男'),
        ('female','女')
    )
    #nick name
    nick_name = models.CharField(max_length=64,verbose_name='昵称',default='')
    #birthday
    birthday = models.DateField(verbose_name='生日',null=True,blank=True)
    #sex
    gender = models.CharField(
        max_length=32,
        verbose_name='性别',
        choices=GENDER_CHOICES,
        default='female'
    )
    #address
    address = models.CharField(max_length=128,verbose_name='地址',default='')
    #phone number
    mobile = models.CharField(max_length=11,null=True,blank=True)
    #avater
    image = models.ImageField(
        upload_to='image/%Y/%m',
        default='image/default.png',
        max_length=128
    )
    #meta information,background column name
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


#Email Verification Code
class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('register','注册'),
        ('forget','找回密码')
    )
    code = models.CharField(max_length=32,verbose_name='验证码')
    email = models.EmailField(max_length=64,verbose_name='邮箱')
    send_type = models.CharField(choices=SEND_CHOICES,max_length=32)
    #now need remove(),otherwise,this will be compile time instead of instantiation time
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

#轮播图 model

class Banner(models.Model):
    title = models.CharField(max_length=128,verbose_name='标题')
    image = models.ImageField(
        upload_to='banner/%Y/%m',
        verbose_name='轮播图',
        max_length=132
    )
    url = models.URLField(max_length=256,verbose_name='访问地址')
    index = models.IntegerField(default=128,verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
