from django.db import models
from django.urls import reverse
import datetime
# Create your models here.

class Category(models.Model):
    'Category for product'
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.name+'-'+self.brand

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    ram=models.CharField(max_length=50,blank=True)
    rom=models.CharField(max_length=50,blank=True)
    cpu=models.CharField(max_length=50,blank=True)
    gpu=models.CharField(max_length=50,blank=True)
    display=models.CharField(max_length=50,blank=True)
    description=models.CharField(max_length=50,default='Short Description About The Product')
    image_main=models.ImageField(upload_to='products')
    
    class Meta:
        ordering=['-id']

    def get_absolute_url(self):
        return reverse("store:product-detail", kwargs={"id": self.id})
    def create_order(self):
        return reverse("store:create-order", kwargs={"id": self.id})

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=50)
    customer_phone=models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    address = models.CharField(max_length=50,default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
