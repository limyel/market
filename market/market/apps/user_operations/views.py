from django.shortcuts import render
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response

from .models import Favorite, Address
from .serializer import FavoritesSerializer, AddressSerializer
from goods.models import Good
from goods.serializer import GoodsSerializer

# Create your views here.


class FavoritesList(generics.ListCreateAPIView):

    queryset = Favorite.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        res = []
        favorites = Favorite.objects.filter(user=request.user)
        for instance in favorites:
            good = Good.objects.get(id=instance.good.id)
            good = GoodsSerializer(good).data
            good['images'][0]['image'] = 'http://127.0.0.1:8000' + good['images'][0]['image']
            good['detail'] = 'http://127.0.0.1:8000' + good['detail']
            res.append(good)
        return Response(res)


class FavoritesDetail(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = Favorite.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'good'
    lookup_url_kwarg = 'good_id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        res = {}
        instance = Favorite.objects.filter(user=request.user, good__id=kwargs.get('good_id', 0))
        if len(instance) > 0:
            res['code'] = 0
            good_id = instance[0].good.id
            good = Good.objects.get(id=good_id)
            res['good'] = GoodsSerializer(good).data
        else:
            res['code'] = 1
        return Response(res)


class AddressList(generics.ListCreateAPIView):

    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class AddressDetail(generics.DestroyAPIView):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'