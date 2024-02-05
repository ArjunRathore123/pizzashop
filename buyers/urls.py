from .views import home,menu,register,login,registered
from django.urls import path

urlpatterns = [
    path('home/', home,name='home'),
    path('home/menu/',menu,name='menu'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('register',registered,name='signup')
]