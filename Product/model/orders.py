from django.db import models
from .product import Product
from .register import Register
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    register = models.ForeignKey(Register, on_delete=models.CASCADE)
    address = models.CharField(max_length=25,default='')
    number = models.IntegerField()
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today())