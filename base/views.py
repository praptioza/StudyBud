from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic
from .forms import RoomForm

# view for login
def loginPage(request):
    # print("Login page called")
    # check when pagename is 'login'
    page = 'login'
    # if the user is already logged in, the user cannot login again
    if request.user.is_authenticated:
        return redirect('home')
    
    # # if the request is POST, ie form submission, then get the data of the form fields 
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

    #     # check if there is an entry in the database for that particular user, if not give flash error message
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")

        # authenticate the entered credentials with the credentials stored in the database and if they match, login in the user and  send to the home page, else give flash error message
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist.')

    context = {'page' : page}
    # print("Context:", context)  # Debug print
    return render(request, 'base/login_register.html', context)


# view for logout
def logoutUser(request):
    logout(request)
    return redirect('home')

# view for registration of a new user
def registerPage(request):
    # when the view is accessed via a GET request, i.e, when the user first navigates to the registration page, an empty 'UserCreationForm' instance is created
    form = UserCreationForm()

    # if the form is being submitted via a POST request, 
    if request.method == 'POST':
        # the form is populated with data submitted by the user request.POST
        form = UserCreationForm(request.POST)

        # when form is valid according to rules of UserCreationForm
        if form.is_valid():
            # creates new User object but does not save it to the database immediately
            user = form.save(commit = False)
            # converts username to lowercase to ensure uniqueness
            user.username = user.username.lower()
            # then saves User object to the database
            user.save()
            # once the data is saved, it automatically logs in the user 
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')
    context = {'form' : form}
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(Q(topic__name__icontains = q)|
                                Q(name__icontains = q)|
                                Q(description__icontains = q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms' : rooms, 'topics': topics, 'room_count' : room_count}
    return render(request, 'base/home.html', context)


# view to get all rooms
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)

# view to create a room but only by an autheticated user - CREATE
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


# view to update existing rooms - EDIT
@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here.')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

# view to delete existing rooms - DELETE
@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here.')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})