from django.urls import path

from .views import FavoritesDetail, FavoritesList, AddressList, AddressDetail


urlpatterns = [
    path('', FavoritesList.as_view()),
    path('<int:good_id>/', FavoritesDetail.as_view()),
    path('address/', AddressList.as_view()),
    path('address/<int:id>/', AddressDetail.as_view())
]