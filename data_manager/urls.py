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

    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),

    path('cases/<int:pk>/assign/', views.assignOfficer, name='assign-officer'),
    path('cases/<int:pk>/', views.caseDetail, name='case-detail'),
    path('dashboard/officer/', views.officer_dashboard, name='officer-dashboard'),
    path('dashboard/', views.redirect_dashboard, name='dashboard-redirect'),
    path('cases/<int:pk>/update-status/', views.updateCaseStatus, name='case-update-status'),
    path('dashboard/citizen/', views.citizen_dashboard, name='citizen-dashboard'),
    path('dashboard/commander/', views.commander_dashboard, name='commander-dashboard'),
    path('officer/<int:pk>/', views.officer_profile, name='officer-profile'),
    path('citizen/<int:pk>/', views.view_citizen_profile, name='citizen-profile'),
    path('profile/edit/', views.update_profile, name='edit-profile'),
    path('case/<int:pk>/upload-evidence/', views.upload_evidence, name='upload-evidence'),

    ]