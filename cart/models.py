from django.db import models
from tienda.models import product
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    
   
class cartItem(models.Model):
    amount=models.IntegerField()
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    