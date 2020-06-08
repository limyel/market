import time

from rest_framework import serializers

from goods.models import Good
from goods.serializer import GoodsSerializer
from .models import ShoppingCart, OrderGood, Order
from .utils.alipay import AliPay


class ShoppingCartSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    good = serializers.PrimaryKeyRelatedField(required=True, queryset=Good.objects.all())
    good_num = serializers.IntegerField()
    # good = GoodsSerializer()

    def create(self, validated_data):
        user = self.context['request'].user
        good = validated_data['good']
        good_num = validated_data['good_num']

        existed = ShoppingCart.objects.filter(user=user, good=good)
        if existed:
            existed = existed[0]
            existed.good_num = good_num
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        instance.good_num = validated_data.get('good_num', 0)
        instance.save()
        return instance


class OrderGoodsSerialzier(serializers.ModelSerializer):
    good = GoodsSerializer(many=False)

    class Meta:
        model = OrderGood
        fields = "__all__"


class OrderDetailsSerializer(serializers.ModelSerializer):
    ordergood_set = OrderGoodsSerialzier(many=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self, obj):
        alipay = AliPay(
            appid="2016101800718822",
            app_notify_url="http://47.92.87.172:8000/alipay/return/",
            app_private_key_path='keys/private2048.txt',
            alipay_public_key_path='keys/public2048.txt',  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://47.92.87.172:8000/alipay/return/"
        )

        url = alipay.direct_pay(
            subject=obj.order_no,
            out_trade_no=obj.order_no,
            total_amount=obj.mount,
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

        return re_url

    class Meta:
        model = Order
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    status = serializers.CharField(read_only=True)
    pay_no = serializers.CharField(read_only=True)
    order_no = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    alipay_url = serializers.SerializerMethodField(read_only=True)

    def get_alipay_url(self, obj):
        alipay = AliPay(
            appid="2016101800718822",
            app_notify_url="http://47.92.87.172:8000/alipay/return/",
            app_private_key_path='keys/private2048.txt',
            alipay_public_key_path='keys/public2048.txt',  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://47.92.87.172:8000/alipay/return/"
        )

        url = alipay.direct_pay(
            subject=obj.order_no,
            out_trade_no=obj.order_no,
            total_amount=obj.mount,
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

        return re_url


    def generate_order_no(self):
        # 当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        order_no = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id, ranstr=random_ins.randint(10, 99))

        return order_no

    def validate(self, attrs):
        attrs["order_no"] = self.generate_order_no()
        return attrs

    class Meta:
        model = Order
        fields = "__all__"


