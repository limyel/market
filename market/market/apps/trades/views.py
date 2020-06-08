import datetime, time

from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ShoppingCartSerializer, OrdersSerializer, OrderDetailsSerializer
from .models import ShoppingCart, Order, OrderGood
from .utils.alipay import AliPay

# Create your views here.


class ShoppingCartList(generics.ListCreateAPIView):

    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class ShoppingCartDetail(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = ShoppingCartSerializer
    lookup_field = 'good'
    lookup_url_kwarg = 'good_id'

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class OrderViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """
    订单管理
    list:
        获取个人订单
    delete:
        删除订单
    create：
        新增订单
    """
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailsSerializer
        return OrdersSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_good = OrderGood()
            order_good.good = shop_cart.good
            order_good.good_num = shop_cart.good_num
            order_good.order = order
            order_good.save()

            shop_cart.delete()
        return order


class AlipayView(APIView):
    def get(self, request):
        """
        处理支付宝的return_url返回
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="2016101800718822",
            app_notify_url="http://47.92.87.172:8000/alipay/return/",
            app_private_key_path='/Users/limyel/Desktop/market/market/apps/trades/keys/private2048.txt',
            alipay_public_key_path='/Users/limyel/Desktop/market/market/apps/trades/keys/public2048.txt',  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://47.92.87.172:8000/alipay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_no = processed_dict.get('out_trade_no', None)
            pay_no = processed_dict.get('trade_no', None)
            status = processed_dict.get('trade_status', None)

            existed_orders = Order.objects.filter(order_no=order_no)
            for existed_order in existed_orders:
                existed_order.status = 1
                existed_order.pay_no = pay_no
                existed_order.pay_time = datetime.now()
                existed_order.save()

            response = redirect("index")
            response.set_cookie("nextPath","pay", max_age=3)
            return response
        else:
            response = redirect("index")
            return response

    def post(self, request):
        """
        处理支付宝的notify_url
        :param request:
        :return:
        """
        processed_dict = {}
        for key, value in request.POST.items():
            processed_dict[key] = value

        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="2016101800718822",
            app_notify_url="http://47.92.87.172:8000/alipay/return/",
            app_private_key_path='/Users/limyel/Desktop/market/market/apps/trades/keys/private2048.txt',
            alipay_public_key_path='/Users/limyel/Desktop/market/market/apps/trades/keys/public2048.txt',  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://47.92.87.172:8000/alipay/return/"
        )

        verify_re = alipay.verify(processed_dict, sign)

        if verify_re is True:
            order_no = processed_dict.get('out_trade_no', None)
            pay_no = processed_dict.get('pay_no', str(int(time.time())))
            status = processed_dict.get('trade_status', 1)

            existed_orders = Order.objects.filter(order_no=order_no)
            for existed_order in existed_orders:
                order_goods = existed_order.ordergood_set.all()
                for order_good in order_goods:
                    good = order_good.good
                    good.sold_num += order_good.good_num
                    good.save()

                existed_order.pay_status = 1
                existed_order.trade_no = pay_no
                existed_order.pay_time = datetime.now()
                existed_order.save()

            return Response("success")


def Ok(request, id):

    if request.method == 'GET':
        order = Order.objects.get(id=id)
        order.status = 1
        order.save()
        return HttpResponse({})


class Order0List(generics.ListAPIView):

    serializer_class = OrderDetailsSerializer

    def get_queryset(self):
        return Order.objects.filter(status=0, user=self.request.user)


class Order1List(generics.ListAPIView):

    serializer_class = OrderDetailsSerializer

    def get_queryset(self):
        return Order.objects.filter(status=1, user=self.request.user)