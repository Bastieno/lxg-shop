from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  image_url = models.CharField(max_length=1000)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  date_created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name

