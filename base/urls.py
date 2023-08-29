from rest_framework import routers
from django.urls import path, include
from .views import ContactViewSet
router = routers.DefaultRouter()
router.register('contact', ContactViewSet)
urlpatterns = [
    path('', include(router.urls))
]
