from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_creator",
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        # this will make the plural of product as products
        verbose_name_plural = "Products"
        # this will order the products in descending order of creation
        ordering = ("-created",)

    def get_absolute_url(self):
        # reverse is used to get the url of the product_detail view,
        # store is the namespace, product_detail is the name of the view
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title