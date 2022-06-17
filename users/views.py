from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout,get_user_model

User=get_user_model()

# Create your views here.
def login_view(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        
        user = authenticate(request,email=email,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("/")
            else:
                return render(request,"login.html",{"error":"Inactive account"})
            
        return render(request,"login.html",{"error":"Invalid credentials"})
    if request.user.is_authenticated:
        return redirect("/")
    return render(request,"login.html")


def logaut_view(request):
     if request.user.is_authenticated:
            logout(request)
            return redirect("/")
    

def sungup_view(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password=request.POST["password"]
        password_confimation=request.POST["password_confimation"]
        email=request.POST["email"]
        
        if password_confimation!=password:
            return render("/registro_user.html",{"error":"La contraseña no concuerda"})
        
        try:
            new_user=User.objects.create_user(username,email,password)
            new_user.first_name=first_name
            new_user.lastname=last_name
            new_user.save()
            login(request,new_user)
            return redirect("/")
        except IntegrityError:
            return render(request,"/registro_user.html",{"error":"El usuario ya esta registrado"})
        
    return render(request,"/registro_user.html")
            
            
         
        