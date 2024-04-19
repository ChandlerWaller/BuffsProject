from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.http import HttpResponse
from .models import *
from .forms import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def scrap(request):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
# Create your views here.
def index(request):
# Render index.html
    available_shifts = Shift.objects.all().filter(is_available=True)
    print("active shift query set", available_shifts)
    usersname = request.user.username
    return render( request, 'buffs_app/index.html',{'available_shifts':available_shifts, 'usersname':usersname})

def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        user_data = request.POST.copy()
        form = LoginForm(user_data)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend=None)
                return redirect('/')
            else:
                context = {'form':form}
                return render(request, 'buffs_app/login.html', context)
            
    context = {'form':form}
    return render(request, 'buffs_app/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def createShift(request):
    form = ShiftForm()

    if request.method == "POST":
        shift_data = request.POST.copy()
        form = ShiftForm(shift_data)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.username = request.user.username
            shift.save()

            return redirect('/')
        
    context = {'form': form}
    return render(request, 'buffs_app/create_shift.html', context)

def updateShift(request, pk):
    form = ShiftForm()
    shift = Shift.objects.get(id=pk)

    if request.method == "POST":
        shift_data = request.POST.copy()
        form = ShiftForm(shift_data)
        if form.is_valid():
            shift.date = form.cleaned_data.get('date')
            shift.time = form.cleaned_data.get('time')
            shift.is_available = form.cleaned_data.get('is_available')
            shift.position = form.cleaned_data.get('position')
            shift.save()

            return redirect('/')
    else:
        form = ShiftForm(initial={'date':shift.date, 'time':shift.time, 'is_available':shift.is_available})
        
    context = {'form': form}
    return render(request, 'buffs_app/update_shift.html', context)

def deleteShift(request, pk):
    form = ShiftForm()
    shift = Shift.objects.get(id=pk)

    if request.method == "POST":
        shift.delete()
        return redirect('/')
        
    context = {'form':form, 'shift':shift}
    return render(request, 'buffs_app/delete_shift.html', context)

def myshifts(request):
    my_shifts = Shift.objects.all().filter(username=request.user.username)
    print("my shift query set", my_shifts)
    return render( request, 'buffs_app/myshifts.html',{'my_shifts':my_shifts})

def register(request):
    form = LoginForm()

    if request.method == "POST":
        user_data = request.POST.copy()
        form = LoginForm(user_data)
        if form.is_valid():
            username = request.POST["Username"]
            password = request.POST["Password"]
            User.objects.create_user(username, email=None, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user, backend=None)
                return redirect('/')
            else:
                context = {'form':form}
                return render(request, 'buffs_app/register.html', context)
            
    context = {'form':form}
    return render(request, 'buffs_app/register.html', context)

def takeShift(request, pk):
    form = TakenShiftForm()
    shift = Shift.objects.get(id=pk)

    if request.method == "POST":
        shift_data = request.POST.copy()
        form = TakenShiftForm(shift_data)
        if form.is_valid():
            shift.Taken_By = form.cleaned_data.get('Taken_By')
            shift.save()

            return redirect('/')
    else:
        form = TakenShiftForm(initial={'Taken_By':request.user.username})
        
    context = {'form': form}
    return render(request, 'buffs_app/take_shift.html', context)

def shiftdetail(request, pk):
    shift = Shift.objects.get(id=pk)