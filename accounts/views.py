from sponser.models import Sponser
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request, user)
                messages.success(request, "you logged in successfully", 'success')
                return redirect('sponser:sponser_profile')
            else:
                messages.error(request, "username or password is wrong", 'danger')

    elif request.method == 'GET':
        form = LoginForm()
    else:
        form = None 
    
    return render(request,'accounts/login.html',{'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            sponser = Sponser(user=user)
            sponser.save()
            messages.success(request, 'user created, you can log in now!', 'success')
            return redirect('accounts:user_login')
                
    elif request.method == 'GET':
        form = RegisterForm()
    else:
        form = None

    return render(request, 'accounts/register.html', {'form':form})

def user_logout(request):
    logout(request)
    messages.warning(request,'you logged out!', 'warning')
    return redirect('accounts:user_login')