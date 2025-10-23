from django.contrib import admin
from .models import Category

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('category_name', 'created_at')
    list_filter = ( 'is_active', 'created_at')
    search_fields = ( 'category_name', 'description')
    prepopulated_fields = { 'slug': ('category_name', )}
    # auto fill slug when you type category name
    ordering =('category_name',)
    list_per_page = 20

