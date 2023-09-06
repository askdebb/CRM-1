from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('form-employee/', views.employee_form, name='form_employee'),
    path('supervisor/', views.getSupervisorApi, name='supervisor'),
    path('all-workers/', views.allworkers, name='all_workers'),
    
    
    
    path('login-e/', views.employee_login, name='login_e'),
    path('logout-e/', views.log_out, name='logout_e'),
    path('reg-e/', views.reg_employee, name='reg_e'),
    
]