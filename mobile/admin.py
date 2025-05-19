from django.contrib import admin

from .models import Product, ProductImageModel



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'inventory', 'price_main','created_date']
    search_fields = ['title', 'inventory', 'price_main']
    list_per_page = 10
    list_filter = ['title', ]
    prepopulated_fields = {
        'slug':['title']
    }
