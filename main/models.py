from django.db import models
from django.contrib.auth.models import AbstractUser




class Diller(models.Model):
    company_name = models.CharField(max_length=50)
    foto = models.ImageField( upload_to='media', height_field=None, width_field=None, max_length=None)
    ball = models.IntegerField(max_length=5)

    def __str__(self):
        return self.company_name
    

class Product(models.Model):
    diller = models.ForeignKey(Diller,on_delete=models.CASCADE,related_name='diller_product')
    product_name = models.CharField(max_length=250)
    product_weight = models.FloatField()
    product_price = models.FloatField()
    product_quantity = models.FloatField()
    
    def __str__(self):
        return self.product_name
    
# Login section
