from django.db import models
from datetime import datetime
# Create your models here.

#城市字典
class CityDict(models.Model):
    name = models.CharField(max_length=32,verbose_name='城市')
    #城市描述，不一定展示
    desc = models.TextField(verbose_name='描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

#课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=64,verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    image = models.ImageField(
        upload_to='org/%Y/%m',
        verbose_name='封面图',
        max_length=100
    )
    address = models.CharField(max_length=128,verbose_name='机构地址')
    #一个城市可以有很多机构，将city设置成外键
    city = models.ForeignKey(CityDict,verbose_name='所在城市')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

#讲师
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name='所属机构')
    name = models.CharField(max_length=64,verbose_name='教师名称')
    work_years = models.IntegerField(default=0,verbose_name='工作年限')
    work_company = models.CharField(max_length=64,verbose_name='就职公司')
    work_position = models.CharField(max_length=64,verbose_name='公司职位')
    points = models.CharField(max_length=128,verbose_name='教学特点')
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

