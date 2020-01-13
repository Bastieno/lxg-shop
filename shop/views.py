from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
  products = Product.objects.all()
  # output = ', '.join([product.name for product in products])
  return render(request, 'shop/index.html', {'products': products })


def detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  return render(request, 'shop/detail.html', {'product': product})

