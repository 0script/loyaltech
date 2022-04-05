from django.db import models
import datetime
# Create your models here.

class Category(models.Model):
    'Category for product'
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=20,blank=True)


class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    remise=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    ram=models.CharField(max_length=50,blank=True)
    rom=models.CharField(max_length=50,blank=True)
    cpu=models.CharField(max_length=50,blank=True)
    image_main=models.ImageField(upload_to='products')

class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=50)
    customer_phone=models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    address = models.CharField(max_length=50,default='', blank=True)
    phone = models.CharField(max_length=50,blank=False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
