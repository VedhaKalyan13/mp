from django.db import models
from django.contrib.auth.models import User
 
#Create your models here.

 
class Product(models.Model):
    ProductName = models.CharField(max_length=200,null=True)
    ProductId  = models.IntegerField(max_length=50,null=True)
    Quantity  = models.IntegerField(null=True)
    Price  = models.IntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
 
    def __str__(self):
        return self.ProductName



class Stock(models.Model):
    StockId = models.IntegerField(max_length=50,null=True)
    ProductId  = models.IntegerField(max_length=50,null=True)
    StockName = models.CharField(max_length=200,null=True)
    No_of_units  = models.IntegerField(null=True)
    CATERGORY = models.CharField(max_length=100,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.StockId)
 
