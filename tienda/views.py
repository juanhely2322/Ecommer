from unicodedata import category
from django.shortcuts import render

from tienda.models import product

# Create your views here.
def mostrar(request):
   
    #products=product.objects.filter(product_category=1)
    products=product.objects.all()
    return render (request,"home.html",{"products":products})

