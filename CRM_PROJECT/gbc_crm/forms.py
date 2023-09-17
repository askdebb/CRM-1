from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import  Employee, Supervisor

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'


        self.fields['first_name'].label = ''
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'

        self.fields['last_name'].label = ''
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'

        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'

        
        
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Contains uppercase, lower, symbols, numbers, 8+ characters</small></span>'

        
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification</small></span>'

        
        
    
class DateInputField(forms.DateInput):
    input_type = 'date' 

class EmployeeSelectForm(forms.ModelForm):
    first_name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    email_address = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control'}) )
    contact_no = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    date_of_birth = forms.DateField(widget=DateInputField(attrs={'class': 'form-control'}) )
    date_employed = forms.DateField(widget=DateInputField(attrs={'class': 'form-control'}) )
    # user = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True))

    class Meta:
        model = Employee
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(EmployeeSelectForm, self).__init__(*args, **kwargs)
        
        self.fields['supervisor'].queryset = Supervisor.objects.none()
        # self.fields['user'].queryset = User.objects.get([0])
      
  
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['supervisor'].queryset = Supervisor.objects.filter(department_id=department_id).order_by('first_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['supervisor'].queryset = self.instance.department.supervisor.order_by('first_name')

        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['supervisor'].widget.attrs['class'] = 'form-control'
        self.fields['department'].label = 'Department'
        self.fields['supervisor'].label = 'Supervisor'
        
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['user'].label = 'User'
        