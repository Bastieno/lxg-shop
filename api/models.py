from django.db import models
from tastypie.resources import ModelResource
from shop.models import Category, Product

# Create your models here.



class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        excludes = ('date_created',)
        # allowed_methods = ['get']
