from rest_framework import routers
from django.urls import path, include
from .views import JokesViewSet , LocationsViewSet

router = routers.DefaultRouter()

router.register('joke', JokesViewSet)
router.register('Location', LocationsViewSet
)

urlpatterns = [
    path('', include(router.urls))
]
