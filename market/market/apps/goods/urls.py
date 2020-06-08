from django.urls import path

from .views import SlidesList, CategoriesList, CategoriesDetail, GoodsDetail, SearchList


urlpatterns = [
    path('<int:id>/', GoodsDetail.as_view()),
    path('slides/', SlidesList.as_view()),
    path('categories/', CategoriesList.as_view()),
    path('categories/<int:id>/', CategoriesDetail.as_view()),
    path('<str:keywords>/', SearchList.as_view()),

]