from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
from .forms import  EmployeeSelectForm, UserForm
from .models import Supervisor, Employee


# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        return render (request, 'gbc_crm/index.html', {})
    return redirect ('login_e')


def reg_employee(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '{} registered successfully'.format(request.user.username))
            return redirect('login_e')
        messages.success(request, 'check your forms fields well')
        return render (request, 'gbc_crm/auth/reg-e.html', {'form': form})

    form = UserForm
    return render (request, 'gbc_crm/auth/reg-e.html', {'form': form})

def employee_login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password1']
        user = authenticate(username=username, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, '{} signed in successfully'.format(request.user.username))
            return redirect('home')
        messages.success(request, ' wrong username / password')
        return redirect('login_e')
        # return render (request, 'gbc_crm/auth/login_employee.html', {})
    return render (request, 'gbc_crm/auth/login_employee.html', {})

def log_out(request):
    logout(request)
    return redirect ('login_e') 


def employee_form(request):
    if request.user.is_authenticated:
        form = EmployeeSelectForm
        if request.method == 'POST':  
            form = EmployeeSelectForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ' {} form added successfully'.format(request.user.username)) 
                return redirect('home')
            messages.success(request, 'provide the correct information in the form fields.') 
            return render (request, 'gbc_crm/auth/form_employee.html', {'form': form})
        return render (request, 'gbc_crm/auth/form_employee.html', {'form': form})
    else:
        return redirect ('login_e')

def getSupervisorApi(request):
    data = json.loads(request.body)
    department_id = data["id"]
    supervisor = Supervisor.objects.filter(department__id = department_id)
    
    return JsonResponse(list(supervisor.values("id","first_name")), safe=False)



def allworkers(request):
    workers = Employee.objects.all()
    print(workers)
    context = {
        'workers': workers
    }
    return render (request, 'gbc_crm/workersList.html',context)
