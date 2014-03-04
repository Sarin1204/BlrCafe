from django.db import models
from uuidfield import UUIDField
# Create your models here.
class User(models.Model):
    empid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(max_length=15)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    inventory = models.IntegerField(max_length=5)
    price = models.IntegerField(max_length=10)
    
class Transaction(models.Model):
    orderid = UUIDField(auto=True)
    empid = models.ForeignKey(User)
    productid = models.ForeignKey(Product)
    time = models.DateTimeField()
    quantity = models.IntegerField(max_length=5)
    
    
    