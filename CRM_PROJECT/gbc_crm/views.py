from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import  EmployeeSelectForm


# Create your views here.
def home(request):
    return render (request, 'gbc_crm/index.html', {})


def employee_form(request):
    if request.method == 'POST':
        form = EmployeeSelectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_employee')
    form = EmployeeSelectForm
    return render (request, 'gbc_crm/auth/reg_employee.html', {'form': form})


def employee_form_login(request):
    if request.method == "POST":
        email=request.POST['email_address']
        password=request.POST['password_1']
        employee = authenticate(email=email, password=password)
        if employee is None:
            login(request, employee)
            return redirect('home')
            
    
    
    return render (request, 'gbc_crm/auth/login_employee.html', {})
