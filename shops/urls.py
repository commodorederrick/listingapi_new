from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet, ListingViewSet

router = DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'listings', ListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]