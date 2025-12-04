from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('logOut', views.logOutUser, name='loginOut'),
    path('register', views.registerUser, name='register'),

]
