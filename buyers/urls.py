from .views import home,register,login,registered,handlelogin,handlelogout
from django.urls import path

urlpatterns = [
    path('home/', home,name='home'),
    # path('home/menu/',menu,name='menu'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('register',registered,name='signup'),
    path('login',handlelogin,name='handlelogin'),
    path('logout',handlelogout,name='logout')
]