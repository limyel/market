from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    用户
    """
    phone = models.CharField(max_length=11, verbose_name='手机号')
    password = models.CharField(max_length=64, null=True, blank=True, default='', verbose_name='密码')
    picture = models.ImageField(upload_to='users/picture/%Y/%m/%d/', null=True, blank=True, default='', verbose_name='头像')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.phone


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=8, verbose_name='验证码')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.code
