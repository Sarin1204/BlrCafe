from django.contrib import admin
from Cafe.models import User
from Cafe.models import Product
from Cafe.models import Transaction
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Transaction)