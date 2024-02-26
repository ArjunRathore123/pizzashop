from django.shortcuts import render,redirect
from accounts.models import CustomUser
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages

def menu(request):
    return render(request,'menu.html')