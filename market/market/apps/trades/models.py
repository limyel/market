import time

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Good

# Create your models here.


User = get_user_model()


class ShoppingCart(models.Model):
    """
    购物车
    """
    good_num = models.IntegerField(default=0, verbose_name='商品数量')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='用户')
    good = models.ForeignKey(to=Good, on_delete=models.CASCADE, related_name='shopping_cart', verbose_name='商品')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return F'{self.user.name}-{self.good.name}-{self.good_num}'


class Order(models.Model):
    """
    订单
    """
    STATUS = (
        (0, '待收货'),
        (1, '已完成'),
    )
    PAY = (
        (0, '支付宝'),
        (1, '微信')
    )
    status = models.CharField(max_length=32, choices=STATUS, default=0, verbose_name='订单状态')
    pay = models.CharField(max_length=16, choices=PAY, default=1, verbose_name='支付方式')
    order_no = models.CharField(max_length=64, null=True, blank=True, verbose_name='订单号')
    pay_no = models.CharField(max_length=64, null=True, blank=True, default=str(int(time.time())), verbose_name='交易号')
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    mount = models.FloatField(verbose_name='订单金额')
    remark = models.CharField(max_length=512, blank=True, null=True, verbose_name='备注')
    name = models.CharField(max_length=16, default='', verbose_name='收货人')
    phone = models.CharField(max_length=11, default='', verbose_name='手机号')
    address = models.CharField(max_length=128, default='', verbose_name='地址')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='用户')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.order_no


class OrderGood(models.Model):
    """
    订单中的商品
    """
    SCORE = (
        (0, '差'),
        (1, '好')
    )
    good_num = models.IntegerField(default=0, verbose_name='商品数量')
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='订单')
    good = models.ForeignKey(to=Good, on_delete=models.CASCADE, verbose_name='商品')
    score = models.IntegerField(choices=SCORE, null=True, blank=True, verbose_name='评分')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '订单中的商品'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.order.order_no


class Evaluation(models.Model):
    """
    订单评价
    """
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='订单')
    content = models.CharField(max_length=128, verbose_name='补充')
    score = models.IntegerField(default=5, verbose_name='评分')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '订单评价'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.order.order_no
