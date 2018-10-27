from django.urls import path
from haxtor import views

app_name='haxtor'

urlpatterns = [
    path("register/",views.UserRegister,name = "userRegister"),
    path("login/",views.user_login,name="user_login")
]
