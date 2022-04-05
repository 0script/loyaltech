from django.contrib import admin
from .models import Order,Products,Category

# Register your models here.

admin.site.register(Order)
admin.site.register(Products)
admin.site.register(Category)