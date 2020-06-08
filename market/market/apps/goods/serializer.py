from rest_framework import serializers

from .models import Good, Slide, GoodPicture, Category
# from trades.serializer import ShoppingCartSerializer


class GoodPicturesSerializer(serializers.ModelSerializer):
    """
    商品图片
    """
    class Meta:
        model = GoodPicture
        fields = ['image', ]


class GoodsSerializer(serializers.ModelSerializer):
    """
    商品序列化器
    """
    images = GoodPicturesSerializer(many=True, read_only=True)
    # shopping_cart = ShoppingCartSerializer(many=True)

    class Meta:
        model = Good
        fields = ['id', 'images', 'name', 'short', 'detail', 'weight', 'production', 'quantity', 'discount', 'price']


class SlidesSerializer(serializers.ModelSerializer):
    """
    活动
    """
    goods = GoodsSerializer(many=True, read_only=True)

    class Meta:
        model = Slide
        fields = ['id', 'title', 'image', 'goods']


class CategoriesSerializer(serializers.ModelSerializer):
    """
    分类
    """
    goods = GoodsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'goods']