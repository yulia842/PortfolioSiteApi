from rest_framework import routers
from django.urls import path, include
from .views import JokeViewSet , LocationViewSet

router = routers.DefaultRouter()

router.register('joke', JokeViewSet)
router.register('Location', LocationViewSet
)

urlpatterns = [
    path('', include(router.urls))
]
