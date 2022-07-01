from django.shortcuts import redirect, render
from .models import Cart, cartItem
from tienda.models import product

# Create your views here.

def get_cart (request):
    if request.user.is_authenticated:
        products=request.user.cart.products.all()
        return render(request,"cart.html",{"products":products})
    return redirect("/")

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


def delete_from_cart(request,idCartItem):
     if request.user.is_authenticated:
         caritem= cartItem.objects.get(pk=idCartItem)
         if caritem.cart.user==request.user:
            caritem.delete()
         return redirect("/cart")
     return redirect("/")
