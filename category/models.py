from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length =50, unique = True)
    slug = models.SlugField(max_length =50, unique = True)
    description = models.TextField( blank=True, null= True)
    Category_image = models.ImageField(upload_to="images/category" , null = True)
    is_active = models.BooleanField(default=True)
    created_at =models.DateTimeField(auto_now_add=True, blank= True, null=True)
    updated_at =models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['-created_at']