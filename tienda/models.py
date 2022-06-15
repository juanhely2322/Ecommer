from dataclasses import field
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=120,verbose_name="name", null=True)
    price=models.FloatField(null=True)
    descripcion=models.CharField(max_length=100)
    image=models.CharField(max_length=220,null=True)
   #amount=models.IntegerField(null=True)
    def __str__(self):
        return self.name
    
    
class category(models.Model):
    name_category=models.CharField(max_length=60) 
    products=models.ManyToManyField(product,related_name="product_category")
    def __str__(self):
        return self.name_category   
   