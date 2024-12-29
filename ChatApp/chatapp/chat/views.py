from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import chatGroupForm
from .models import chatGroup, Usergroup
@login_required
def index(request):
    user_groups = Usergroup.objects.filter(user=request.user, is_approved=True)
    admin_groups = chatGroup.objects.filter(admin=request.user)
    
    return render(request, "chat/index.html", {
        "user_groups": user_groups,
        "admin_groups": admin_groups,
    })


@login_required
def room(request, room_name):
    chat_group = get_object_or_404(chatGroup, name=room_name)
    is_admin = request.user == chat_group.admin
    return render(request, "chat/room.html", {
        "room_name": room_name,
        "is_admin": is_admin,
        "chat_group": chat_group,
    })

@login_required
def create_chat_group(request):
    if request.method == 'POST':
        form = chatGroupForm(request.POST)
        if form.is_valid():
            chat_group = form.save(commit=False)
            chat_group.admin = request.user
            chat_group.save()
            return redirect('index')
    else:
        form = chatGroupForm()
    
    return render(request, 'chat/create_group.html', {'form': form})

@login_required
def join_chat_group(request):
    if request.method == 'POST':
        group_name = request.POST['group_name']
        try:
            chat_group = chatGroup.objects.get(name=group_name)
            user_group, created = Usergroup.objects.get_or_create(user=request.user, chat_group=chat_group)
            if request.user == chat_group.admin:
                messages.error(request, "You are admin of this group. You cannot send invitiataion.")
            elif created:
                messages.success(request, "Request to join the group has been sent to the admin.")
            else:
                messages.info(request, "You have already requested to join this group.")
        except chatGroup.DoesNotExist:
            messages.error(request, "Group does not exist.")
    return redirect('index')
    
@login_required  
def approve_user(request, group_id, user_id):
    chat_group = get_object_or_404(chatGroup, id=group_id)
    user_chat_group = get_object_or_404(Usergroup, chat_group=chat_group, user_id=user_id)
    
    if request.user == chat_group.admin:
        user_chat_group.is_approved = True
        user_chat_group.save()

    return redirect('room', room_name=chat_group.name)

@login_required
def members(request, group_id):
    chat_group = get_object_or_404(chatGroup, id=group_id)
    members = Usergroup.objects.filter(chat_group=chat_group, is_approved=True)
    
    return render(request, 'chat/members.html', {
        'chat_group': chat_group,
        'members': members,
    })

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

@login_required
def pending_requests(request, group_id):
    chat_group = get_object_or_404(chatGroup, id=group_id)
    if request.user != chat_group.admin:
        return redirect('index')
    
    join_requests = Usergroup.objects.filter(chat_group=chat_group, is_approved=False)
    
    return render(request, 'chat/pending_requests.html', {
        'chat_group': chat_group,
        'join_requests': join_requests,
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
