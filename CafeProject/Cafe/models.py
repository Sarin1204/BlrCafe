from django.db import models
from django.contrib import admin
from CafeProject import settings
from uuidfield import UUIDField

# Create your models here.
class User(models.Model):
    empid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(max_length=15)
    password = models.CharField(max_length=50)
    credits = models.IntegerField(max_length=5)
    photo = models.ImageField(upload_to='users',blank = True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    PRODUCT_TYPES = (
        ('Chips', 'Chips'),
        ('Beverages', 'Beverages'),
        ('Biscuits', 'Biscuits'),
        ('Chocolates', 'Chocolates'),
        ("Heat'n'Eat", "Heat'n'Eat"),
    )
    
    name = models.CharField(max_length=50)
    inventory = models.IntegerField(max_length=5)
    price = models.IntegerField(max_length=10)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    photo = models.ImageField(upload_to='products',blank = True)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    transactionid=models.AutoField(primary_key=True)
    orderid = models.CharField(max_length=100)
    empid = models.ForeignKey(User)
    productid = models.ForeignKey(Product)
    time = models.DateTimeField()
    quantity = models.IntegerField(max_length=5)
    totalprice = models.IntegerField(max_length=10)
    def __str__(self):
        return self.empid.name