from django.urls import path

from .views import ShoppingCartList, ShoppingCartDetail, Ok, Order0List, Order1List


urlpatterns = [
    path('shopping_carts/', ShoppingCartList.as_view()),
    path('shopping_carts/<int:good_id>/', ShoppingCartDetail.as_view()),
    path('<int:id>/', Ok),
    path('order_0/', Order0List.as_view()),
    path('order_1/', Order1List.as_view())
]