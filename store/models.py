from django.db import models
from django.utils.text import slugify
from django.conf import settings
from category.models import Category


class Product(models.Model):
    # 🧩 Basic Info
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    # 💰 Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # 🏷️ Stock & Category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    # 🖼️ Media
    thumbnail = models.ImageField(upload_to='products/thumbnails/', blank=True, null=True)

    # 👤 Tracking
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Auto-generate slug if not set"""
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            # ensure unique slug
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def get_final_price(self):
        """Returns discounted price if available"""
        return self.discount_price if self.discount_price else self.price
