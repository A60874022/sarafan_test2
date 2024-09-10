from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Модель, представляющая категории."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Модель, представляющая подкатегории."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="subcategories/")
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель, представляющая продукты."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image_left = models.ImageField(upload_to="products/left/")
    image_right = models.ImageField(upload_to="products/right/")
    image_above = models.ImageField(upload_to="products/above/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(
        Subcategory, related_name="products", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Cart(models.Model):
    """Модель, представляющая корзины."""

    user = models.ForeignKey(
        User,
        verbose_name="пользователь",
        on_delete=models.CASCADE,
    )


class CartItem(models.Model):
    """Модель, представляющая продукты в корзине."""

    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
