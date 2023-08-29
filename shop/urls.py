from rest_framework import routers
from django.urls import path, include
from .views import ProductViewSet, CartViewSet

router = routers.DefaultRouter()
router.register('product',ProductViewSet)
router.register('cart',CartViewSet)
urlpatterns = [
    path('',include(router.urls)),
]