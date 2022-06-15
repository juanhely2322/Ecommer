from django.urls import path
from tienda.views import mostrar

urlpatterns = [
   
    path("",mostrar)
]