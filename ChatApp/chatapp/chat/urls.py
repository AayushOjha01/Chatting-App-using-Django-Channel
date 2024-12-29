from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('user/login/', views.login_view, name='login'),
    path('user/signup/', views.signup_view, name='signup'),
    path('user/logout/', views.logout_view, name='logout'),
    path('create/', views.create_chat_group, name='create_chat_group'),
    path('user/join/', views.join_chat_group, name='join_chat_group'),
    path('approve/<int:group_id>/<int:user_id>/', views.approve_user, name='approve_user'),
    path('pending_requests/<int:group_id>/', views.pending_requests, name='pending_requests'),
    path('members/<int:group_id>/', views.members, name='members'),  # Add this line
]