"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter

from trades.views import OrderViewset




router = DefaultRouter()

# 购物车url
# router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

# 订单相关url
router.register(r'orders', OrderViewset, basename="orders")


schemas_view = get_schema_view(title='market api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('schema/', schemas_view),
    path('goods/', include('goods.urls')),
    path('users/', include('users.urls')),
    path('trades/', include('trades.urls')),
    path('user_operations/', include('user_operations.urls')),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
