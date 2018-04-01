from django.db import models
from datetime import datetime

# Create your models here.
#课程表信息
class Course(models.Model):
    DEGREE_CHOICES = (
        ('cj','初级'),
        ('zj','中级'),
        ('gj','高级')
    )
    name = models.CharField(max_length=64,verbose_name='课程名')
    desc = models.CharField(max_length=512,verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=DEGREE_CHOICES,max_length=16)
    #使用分钟做后台记录
    learn_times = models.IntegerField(default=0,verbose_name='学习时长')
    #保存学习人数：点击开始学习计算
    students = models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏人数')
    image = models.ImageField(
        upload_to='courses/%Y/%m',
        verbose_name='封面图',
        max_length=132
    )
    #保存点击量
    click_nums = models.IntegerField(default=0,verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

#章节
class Lesson(models.Model):
    #一个课程可以对应多个章节，所以在章节中将课程设置成外键
    course = models.ForeignKey(Course,verbose_name='课程')
    name = models.CharField(max_length=128,verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

#每章视频
class Video(models.Model):
    #一个章节对应很多视频，所以在视频表中将章节设置为外键
    lesson = models.ForeignKey(Lesson,verbose_name='章节')
    name = models.CharField(max_length=128,verbose_name='视频名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

#课程资源
class CourseResource(models.Model):
    #一个课程对应很多资源，所以将资源设置为外键
    course = models.ForeignKey(Course,verbose_name='课程')
    name = models.CharField(max_length=128,verbose_name='名称')
    #上传的是文件类型
    downlod = models.FileField(
        upload_to='course/resource/%Y/%m',
        verbose_name='资源文件',
        max_length=128
    )
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

