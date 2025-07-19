from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('case/<str:pk>/', views.case, name='case'),
    path('create-case/', views.createCase, name='create-case'),
    path('update-case/<str:pk>/', views.updateCase, name='update-case'),
    path('delete-case/<str:pk>/', views.deleteCase, name='delete-case'),

    path('forum/', views.forumHome, name='forum-home'),
    path('forum/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
     path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    ]