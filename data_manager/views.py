from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .models import Case, CaseType, roomForum, topic, Message
from .forms import CaseForm, RoomForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('forum-home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist. Please register!")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum-home')
        else:
            messages.error(request, "Username or password is incorrect. Please try again!")
    context = {'page': page}
    return render(request, 'data_manager/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration. Please try again!")
    context = {'form': form}
    return render(request, 'data_manager/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    cases = Case.objects.filter(
        Q(case_type__name__icontains=q)
        | Q(title__icontains=q)
        | Q(description__icontains=q)
        | Q(location__icontains=q)
        )
    
    case_count = cases.count()
    case_types = CaseType.objects.all()
    context = {'cases': cases, 'case_types': case_types, 'case_count': case_count}
    return render(request, 'data_manager/home.html', context)
    

def case(request, pk):
    case = Case.objects.get(id=pk)
    context = {'case': case}
    return render(request, 'data_manager/case.html', context)

@login_required(login_url='login')
def createCase(request):
    form = CaseForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after saving the case
    return render(request, 'data_manager/case_form.html', context)

@login_required(login_url='login')
def updateCase(request, pk):
    case = Case.objects.get(id=pk)
    form = CaseForm(instance=case)
    context = {'form': form}

    if request.user != case.user:
        return HttpResponse("You are not allowed to edit this case.")

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after updating the case
    return render(request, 'data_manager/case_form.html', context)

@login_required(login_url='login')
def deleteCase(request, pk):
    case = Case.objects.get(id=pk)

    if request.user != case.user:
        return HttpResponse("You are not allowed to delete this case.")

    if request.method == 'POST':
        case.delete()
        return redirect('home')  # Redirect to home after deleting the case
    return render(request, 'data_manager/delete.html', {'obj': case})




def forumHome(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = roomForum.objects.filter(
        Q(topic__name__icontains=q)
        | Q(name__icontains=q)
        | Q(description__icontains=q)
        )
    
    room_count = rooms.count()
    topics = topic.objects.all()
    forumMessages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'forumMessages': forumMessages}
    # Placeholder for forum home view
    return render(request, 'data_manager/home_forum.html', context)

def room(request, pk):
    room = roomForum.objects.get(id=pk)
    forumMessages = room.message_set.all().order_by('-created_at')
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
                user=request.user,
                room=room,
                body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
        
    context = {'room': room, 'forumMessages': forumMessages, 'participants': participants}
    # Placeholder for forum room view
    return render(request, 'data_manager/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.roomforum_set.all()
    forumMessages = user.message_set.all()
    topics = topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'forumMessages': forumMessages, 'topics': topics}
    return render(request, 'data_manager/profile.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            form.save()
            return redirect('forum-home')  # Redirect to home after saving the case
    return render(request, 'data_manager/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = roomForum.objects.get(id=pk)
    form = RoomForm(instance=room)
    context = {'form': form}

    if request.user != room.host:
        return HttpResponse("You are not allowed to edit this case.")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('forum-home')  # Redirect to home after updating the case
    return render(request, 'data_manager/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = roomForum.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed to delete this case.")

    if request.method == 'POST':
        room.delete()
        return redirect('forum-home')  # Redirect to home after deleting the case
    return render(request, 'data_manager/delete.html', {'obj': room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed to delete this case.")

    if request.method == 'POST':
        message.delete()
        return redirect('forum-home')  # Redirect to home after deleting the case
    return render(request, 'data_manager/delete.html', {'obj': message})