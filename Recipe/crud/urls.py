from django.urls import path, include
from rest_framework import routers
from .views import RecipeViewSet

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
