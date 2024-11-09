from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def home(request):
    return HttpResponse('Home Page')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to the login view after successful registration
    context = {'registerform': form}
    return render(request, 'Users/register.html', context)  # Render the registration form

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("dashboard")  # Redirect to the dashboard after successful login
    context = {'loginform': form}
    return render(request, 'Users/login.html', context)  # Render the login form

def logout(request):
    auth_logout(request)
    return redirect("login")  # Redirect to the login view after logout

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'Users/dashboard.html')  # Render the dashboard view
