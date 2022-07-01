from django.urls import path
from . import views
urlpatterns=[
    path("signup/",views.sungup_view,name="singup"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logaut_view,name="logout")
]