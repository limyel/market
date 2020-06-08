from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import get_code, UserDetail


urlpatterns = [
    path('', UserDetail.as_view()),
    path('registerlogin/', obtain_jwt_token),
    path('getcode/', get_code),
]