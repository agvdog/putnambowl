from django.urls import path
from .views import*

app_name = "main"

urlpatterns = [
    path("",index, name="index"),
    path("homepage/",homepage,name="homepage"),
    path("pickform/",pickform,name="pickform"),
    path("preseason/",preseason,name="preseason"),
    path("pickhistory/",pickhistory,name="pickhistory"),
    path("dashboard/",dash,name="dash"),
    path("register/",register_request,name="register"),
    path("rules/",rules,name="rules"),
    path("login/",login_request,name="login"),
    path("logout/",logout_request,name="logout"),
]

