from django.db import models

# Create your models here.


class Good(models.Model):
    """
    商品
    """
    name = models.CharField(max_length=64, verbose_name='商品名')
    price = models.FloatField(verbose_name='原价格')
    discount = models.FloatField(verbose_name='折扣价格')
    short = models.CharField(max_length=32, verbose_name='商品描述')
    detail = models.ImageField(upload_to='goods/detail/%Y/%m/%d/', verbose_name='商品详情')
    weight = models.CharField(max_length=64, verbose_name='重量')
    production = models.CharField(max_length=64, verbose_name='产地')
    quantity = models.IntegerField(verbose_name='限购数量')
    sold_num = models.IntegerField(default=0, verbose_name='销量')
    category = models.ForeignKey(to='Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='goods', verbose_name='分类')
    slide = models.ForeignKey(to='Slide', on_delete=models.SET_NULL, null=True, blank=True, related_name='goods', verbose_name='轮播图对应的活动')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ('created', )

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=16, verbose_name='分类名称')
    isIndex = models.BooleanField(default=False, verbose_name='是否在首页')
    image = models.ImageField(upload_to='goods/categories/images/%Y/%m/%d', null=True, blank=True, verbose_name='分类图片')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        get_latest_by = 'created'
        ordering = ('created', )

    def __str__(self):
        return self.name


class Slide(models.Model):
    """
    轮播图活动
    """
    title = models.CharField(max_length=32, verbose_name='标题')
    image = models.ImageField(upload_to='goods/slide_show/%Y/%m/%d/', default='', verbose_name='图片')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '轮播图对应的活动'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title


class GoodPicture(models.Model):
    """
    商品图片
    """
    good = models.ForeignKey('Good', on_delete=models.CASCADE, related_name='images', verbose_name='商品')
    image = models.ImageField(upload_to='goods/image/%Y/%m/%d/', verbose_name='商品图片')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.good.name