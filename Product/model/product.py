from django.db import models
from .categories import Categories

class Product(models.Model):
    product=models.CharField(max_length=25)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    description=models.CharField(max_length=25)
    price=models.IntegerField()
    img=models.ImageField(upload_to='image')

    def __str__(self):
        return f"{self.product} - {self.category}"


    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)