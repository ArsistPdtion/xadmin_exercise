from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import Course

# Create your models here.

#用户学习表单
class UserAsk(models.Model):
    name = models.CharField(max_length=32,verbose_name='姓名')
    mobile = models.CharField(max_length=11,verbose_name='手机')
    course_name = models.CharField(max_length=64,verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

#用户对于课程评论
class CourseComments(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程')
    user = models.ForeignKey(UserProfile,verbose_name='用户')
    comments = models.CharField(max_length=256,verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='评论时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

#用户对于课程、机构、讲师的收藏
class UserFavorite(models.Model):
    TYPE_CHOICES = (
        (1,'课程'),
        (2,'课程机构'),
        (3,'讲师')
    )

    user = models.ForeignKey(UserProfile,verbose_name='用户')
    fav_id = models.IntegerField(default=0)
    fav_type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
        verbose_name='收藏类型'
    )
    add_time = models.DateTimeField(default=datetime.now,verbose_name='收藏时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

#用户消息表
class UserMessage(models.Model):
    #消息有两种，发送给全员或者发送给某一个用户
    #为0发送给所有的用户，不为0，发送给特定用户
    user = models.ForeignKey(Course,verbose_name='接收用户')
    message = models.TextField(verbose_name='消息内容')
    #是否已读
    has_read = models.BooleanField(default=False,verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

#用户课程表
class UserCourse(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程')
    user = models.ForeignKey(UserProfile,verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name
