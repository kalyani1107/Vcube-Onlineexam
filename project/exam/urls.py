from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('signup',views.signup),
    path('register',views.register),
    path('login',views.loginuser),
    path('adminform',views.adminform,name='adminform'),
    path('create_user',views.create_user,name='create_user')

]