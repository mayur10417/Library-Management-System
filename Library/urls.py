from django.urls import path
from . import views

urlpatterns = [
    path('',views.Library),
    path('login',views.userlogin,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
    path('addbook',views.addbook,name="addbook"),
    path('showbook',views.showbook,name="showbook"),
    path('delete',views.delete,name="delete"),
    path('update',views.update,name="update"),
]