# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Good, GoodPicture, Category, Slide


class GoodAdmin(admin.ModelAdmin):

    list_display = ['name', 'price', 'discount', 'short', 'detail', 'weight', 'production', 'category',
                    'slide']
    search_fields = ['name', 'short']
    list_filter = ['category', 'slide']
    list_per_page = 20
    list_display_links = ['name', ]


class GoodPictureAdmin(admin.ModelAdmin):

    list_display = ['good', 'image']


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'isIndex', 'image']


class SlideAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']


admin.site.register(Good, GoodAdmin)
admin.site.register(GoodPicture, GoodPictureAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Category, CategoryAdmin)