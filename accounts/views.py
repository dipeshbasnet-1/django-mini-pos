from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect("login")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "accounts/register.html", context)

def login_user(request):
    if request.method == "POST":
        form= LoginForm(request, data=request.POST)
        
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login Successfully")
            return redirect("dashboard")
    else:
        form=LoginForm()
                    
    context={"form": form}
    return render (request, 'accounts/login.html',context)

def logout_user(request):
    logout(request)
    return redirect("login")

def dashboard(request):
    return render(request, "accounts/dashboard.html")