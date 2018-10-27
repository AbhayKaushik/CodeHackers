from django.urls import path
from haxtor import views

app_name='haxtor'

urlpatterns = [
    path("register/",views.UserRegister,name = "userRegister"),
    path("login/",views.user_login,name="user_login"),
    path("dashboard/",views.user_dashboard,name="dashboard"),
    path("question/",views.userQuestions,name="testQuestions"),
    path("group1/",views.submitAnswer,name="submitAnswer")
]
