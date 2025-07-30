from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.db.models import Q
from .models import Case, CaseType, roomForum, topic, Message, User
from .forms import CaseForm, RoomForm, UserForm, MyUserCreationForm, AssignOfficerForm, CaseStatusForm



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
            return redirect('dashboard-redirect')
        else:
            messages.error(request, "Username or password is incorrect. Please try again!")
    context = {'page': page}
    return render(request, 'data_manager/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'citizen'
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration. Please try again!")
    context = {'form': form}
    return render(request, 'data_manager/login_register.html', context)

def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.role not in allowed_roles:
                return redirect('home')  # or a custom "Access Denied" page
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

@login_required
@role_required('commander')  # Only station commanders can assign
def assignOfficer(request, pk):
    case = get_object_or_404(Case, id=pk)
    form = AssignOfficerForm(instance=case)

    if request.method == 'POST':
        form = AssignOfficerForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case-detail', pk=pk)  # Go back to case details

    return render(request, 'data_manager/assign_officer.html', {'form': form, 'case': case})

@login_required
def caseDetail(request, pk):
    case = get_object_or_404(Case, id=pk)

    # Restrict access:
    if request.user.role == 'officer' and case.assigned_officer != request.user:
        return redirect('officer-dashboard')
    if request.user.role == 'citizen' and case.user != request.user:
        return redirect('citizen-dashboard')

    return render(request, 'data_manager/case_detail.html', {'case': case})

@login_required
@role_required('officer')
def officer_dashboard(request):
    assigned_cases = Case.objects.filter(assigned_officer=request.user)
    workload_count = assigned_cases.count()

    return render(request, 'data_manager/officer_dashboard.html', {
        'cases': assigned_cases,
        'workload_count': workload_count,
    })

@login_required
def redirect_dashboard(request):
    if request.user.role == 'officer':
        return redirect('officer-dashboard')
    elif request.user.role == 'commander':
        return redirect('commander-dashboard')
    else:
        return redirect('citizen-dashboard')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    cases = Case.objects.filter(
        Q(case_type__name__icontains=q)
        | Q(title__icontains=q)
        | Q(description__icontains=q)
        | Q(city__icontains=q)
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
            case = form.save(commit=False)
            case.user = request.user
            case.save()
            return redirect('home')  

    return render(request, 'data_manager/case_form.html', context)


@login_required(login_url='login')
def updateCase(request, pk):
    case = Case.objects.get(id=pk)
    # Only owner allowed to update

    form = CaseForm(instance=case)
    context = {'form': form}

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            case = form.save(commit=False)
            case.user = request.user  # Ensure the user remains the same
            case.save()
            return redirect('home')  # Redirect after update

    return render(request, 'data_manager/case_form.html', context)


@login_required
@role_required('officer', 'commander')
def updateCaseStatus(request, pk):
    case = get_object_or_404(Case, id=pk)

    # Ensure only assigned officer or commander can update
    if request.user.role == 'officer' and case.assigned_officer != request.user:
        return redirect('officer-dashboard')

    form = CaseStatusForm(instance=case)

    if request.method == 'POST':
        form = CaseStatusForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case-detail', pk=case.id)

    return render(request, 'data_manager/update_status.html', {'form': form, 'case': case})


@login_required
def citizen_dashboard(request):
    cases = Case.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'data_manager/citizen_dashboard.html', {'cases': cases})


@login_required(login_url='login')
@role_required('officer', 'commander')
def deleteCase(request, pk):
    case = Case.objects.get(id=pk)

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

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('user-profile', pk=user.id)
        
    return render(request, 'data_manager/update_user.html', {'form': form})

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = topic.objects.filter(name__icontains=q)
    return render(request, 'data_manager/topics.html', {'topics': topics})

def activityPage(request):
    forumMessages = Message.objects.all()
    return render(request, 'data_manager/activity.html', {'forumMessages': forumMessages})