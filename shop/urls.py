from django.urls import path
from . import views

urlpatterns = [
  path('products', views.index, name='product_index'),
  path('products/<int:product_id>', views.detail, name='product_detail')
]
