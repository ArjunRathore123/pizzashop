from .views import menu
from django.urls import path, include


urlpatterns = [
    path('home/menu',menu,name='menu'),

    
]