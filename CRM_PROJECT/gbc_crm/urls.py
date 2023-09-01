from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('reg-employee/', views.employee_form, name='reg_employee'),
    path('login-employee/', views.employee_form_login, name='login_employee'),
    
]