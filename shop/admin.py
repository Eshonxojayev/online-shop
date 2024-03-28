from django.contrib import admin
from .models import Category, Product, Rate, Profile

admin.site.register(Category)
admin.site.register(Rate)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'rating']
    raw_id_fields = ['category']

admin.site.register(Profile)    
