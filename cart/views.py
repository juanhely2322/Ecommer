from django.shortcuts import redirect, render
from .models import Cart, cartItem
from tienda.models import product
import requests
# Create your views here.

def get_cart (request):
    return render(request,"cart.html")

def add_to_cart(request,idProduct):
    if request.user.is_authenticated:
        cartitem=cartItem()
        cartitem.product=product.objects.get(pk=idProduct)
        cartitem.amount=1
        if request.user.cart:
            cartitem.cart = request.user.cart
        else:
            '''cart = Cart()
            cart.user = request.user
            cart.save()
            cartitem.cart = cart'''
            
            try:
                cartitem = request.user.cart
            except Cart.DoesNotExist:
                cartitem = Cart.objects.create(user=request.user)
              
        
        cartitem.save()
            
    return redirect("/")