from django.db import models

# Create your models here.
class User(models.Model):
    empid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField(max_length=15)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    