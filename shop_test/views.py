from rest_framework import generics, permissions
from .models import Category, Subcategory, Product, Cart, CartItem
from .serializers import (
    CategorySerializer,
    SubcategorySerializer,
    ProductSerializer,
    CartItemSerializer,
    CartSerializer,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from http import HTTPStatus
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с категориями."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class SubcategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с подкатегориями."""

    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = PageNumberPagination


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с продуктами."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class CartViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с корзинами."""

    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=1)  # self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=1)  # self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с конкретной корзиной."""

    serializer_class = CartItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.get(user=1)  # self.request.user)
        return CartItem.objects.filter(cart=cart)

    def create(self, request):
        cart = request.data.get("cart")
        product = request.data.get("product")
        quantity = request.data.get("quantity")
        product_bd = get_object_or_404(Product, name=product)
        cart_bd = get_object_or_404(Cart, id=cart)
        CartItem.objects.create(
            product=product_bd, quantity=quantity, cart=cart_bd
        )

        return Response(status=HTTPStatus.CREATED)

    def update(self, request):
        cart = request.data.get("cart")
        product = request.data.get("product")
        quantity = request.data.get("quantity")
        product_bd = get_object_or_404(Product, name=product)
        cart_product = get_object_or_404(CartItem, product=product_bd, cart=cart)
        cart_product.quantity = int(quantity)
        cart_product.save()
        return Response(status=HTTPStatus.OK)
