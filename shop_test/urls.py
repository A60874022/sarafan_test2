from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    SubcategoryViewSet,
    ProductViewSet,
    CartItemViewSet,
    CartViewSet,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"subcategories", SubcategoryViewSet, basename="subcategories")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"cart-items", CartItemViewSet, basename="cart-items")
router.register(r"cart", CartViewSet, basename="cart")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
