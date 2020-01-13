from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'price')
  exclude = ('date_created', )

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
