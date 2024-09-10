from rest_framework import serializers
from .models import Category, Subcategory, Product, CartItem, Cart
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории."""

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "image"]


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор для подкатегории."""

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Subcategory
        fields = ["id", "name", "slug", "image", "category"]


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продуктов."""

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "image_left",
            "image_right",
            "image_above",
            "price",
            "subcategory",
        ]


class CartItemSerializer(serializers.ModelSerializer):
    """Сериализатор для конкретной корзины."""

    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины."""

    total_items = serializers.SerializerMethodField()
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "user", "total_items", "total_cost"]

    def get_total_items(self, obj):
        return obj.items.count()

    def get_total_cost(self, obj):
        sum_cost = 0
        for item in obj.items.all():
            sum_cost += item.product.price * item.quantity
        return sum_cost
