from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Good

# Create your models here.


User = get_user_model()


class Favorite(models.Model):
    """
    收藏
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='用户')
    good = models.ForeignKey(to=Good, on_delete=models.CASCADE, verbose_name='商品')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name
        ordering = ('-created',)
        unique_together = ('user', 'good')

    def __str__(self):
        return self.good.name


class Address(models.Model):
    """
    收货地址
    """
    name = models.CharField(max_length=16, verbose_name='收货人')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=128, default='', verbose_name='地址')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='用户')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name
        ordering = ('-created_time', )

    def __str__(self):
        return self.name
