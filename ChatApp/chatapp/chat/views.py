from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
@login_required
def index(request):
    return render(request, "chat/index.html")
@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password )
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "chat/login.html")

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if confirm_password != password:
            messages.error(request, "Password didn't match")
        elif User.objects.filter(username= username).exists():
            messages.error(request, "Username already exists")

        else:
            user = User.objects.create_user(username = username, password = password)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")  # Redirect to login view after sign-up
    return render(request, "chat/signup.html")

def logout_view(request):
    logout(request)
    return redirect('login')
