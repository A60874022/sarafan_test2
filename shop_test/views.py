from rest_framework import generics, permissions
from .models import Category, Subcategory, Product, Cart, CartItem
from .serializers import (CategorySerializer, 
                          SubcategorySerializer, 
                          ProductSerializer, 
                          CartItemSerializer,
                           CartSerializer)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = PageNumberPagination

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=1)#self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=1)#self.request.user)

class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart = Cart.objects.get(user=1)#self.request.user)
        return CartItem.objects.filter(cart=cart)
