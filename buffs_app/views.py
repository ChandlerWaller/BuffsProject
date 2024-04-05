from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import ServerForm, ShiftForm
# Create your views here.
def index(request):
# Render index.html
    available_shifts = Shift.objects.all().filter(is_available=True)
    print("active shift query set", available_shifts)
    return render( request, 'buffs_app/index.html',{'available_shifts':available_shifts})

def login():
    return render("Login")

def logout():
    return render("Logout")

def server_detail(request, pk):
    serversShifts = Shift.objects.all()
    print("active Shift query set", serversShifts)
    server = Server.objects.all().filter(id=pk)
    return render( request, 'buffs_app/server_detail.html',{'serversShifts':serversShifts, 'server':server})

def createShift(request, server_id):
    form = ShiftForm()
    server = Server.objects.get(id=server_id)

    if request.method == "POST":
        shift_data = request.POST.copy()
        shift_data['shift_id'] = server_id
        form = ShiftForm(shift_data)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.server = server
            shift.save()

            return redirect('server-detail', server_id)
        
    context = {'form': form}
    return render(request, 'buffs_app/create_shift.html', context)

def updateShift(request, server_id, pk):
    form = ShiftForm()
    server = Server.objects.get(id=server_id)
    shift = Shift.objects.get(id=pk)

    if request.method == "POST":
        shift_data = request.POST.copy()
        shift_data['shift_id'] = server_id
        form = ShiftForm(shift_data)
        if form.is_valid():
            shift.date = form.cleaned_data.get('date')
            shift.time = form.cleaned_data.get('time')
            shift.is_available = form.cleaned_data.get('is_available')
            shift.position = form.cleaned_data.get('position')
            shift.server = server
            shift.save()

            return redirect('server-detail', server_id)
    else:
        form = ShiftForm(initial={'date':shift.date, 'time':shift.time, 'is_available':shift.is_available})
        
    context = {'form': form}
    return render(request, 'buffs_app/update_shift.html', context)

def deleteShift(request, server_id, pk):
    form = ShiftForm()
    shift = Shift.objects.get(id=pk)

    if request.method == "POST":
        shift.delete()
        return redirect('server-detail', server_id)
        
    context = {'form':form, 'shift':shift}
    return render(request, 'buffs_app/delete_shift.html', context)

def updateServer(request, server_id):
    form = ServerForm()
    server = Server.objects.get(id=server_id)

    if request.method == "POST":
        server_data = request.POST.copy()
        server_data['server_id'] = server_id
        form = ServerForm(server_data)
        if form.is_valid():
            server.name = form.cleaned_data.get('name')
            server.save()

            return redirect('server-detail', server_id)
    else:
        form = ServerForm(initial={'name': server.name})
        
    context = {'form': form}
    return render(request, 'buffs_app/update_server.html', context)