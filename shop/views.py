from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
  products = Product.objects.all()
  return render(request, 'shop/index.html', {'products': products })


def detail(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  return render(request, 'shop/detail.html', {'product': product})

