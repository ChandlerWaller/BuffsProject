from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import ShiftForm
# Create your views here.
def index(request):
# Render index.html
    available_shifts = Shift.objects.all().filter(is_available=True)
    print("active shift query set", available_shifts)
    usersname = request.user.username
    return render( request, 'buffs_app/index.html',{'available_shifts':available_shifts, 'usersname':usersname})

def login():
    return render("Login")

def logout():
    return render("Logout")

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