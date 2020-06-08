from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from .serializer import SlidesSerializer, CategoriesSerializer, GoodsSerializer
from .models import Slide, Category, Good

# Create your views here.


class SlidesList(generics.ListAPIView):

    queryset = Slide.objects.all()
    serializer_class = SlidesSerializer


class CategoriesList(generics.ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

    def get(self, request, *args, **kwargs):
        print(request.user.username)
        print(request.user)
        return self.list(request, *args, **kwargs)


class CategoriesDetail(generics.RetrieveAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() if kwargs['id'] != 0 else Category.objects.earliest()
        serializer = self.get_serializer(instance)
        print(request.user.username)
        return Response(serializer.data)


class GoodsDetail(generics.RetrieveAPIView):

    queryset = Good.objects.all()
    serializer_class = GoodsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class SearchList(generics.ListAPIView):

    serializer_class = GoodsSerializer

    def get_queryset(self):
        return Good.objects.filter(name__contains=self.kwargs.get('keywords'))
