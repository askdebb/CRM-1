from django import forms
from django.forms import ModelForm

from .models import  Employee

# class EmployeeForm(ModelForm):
    
class DateInputField(forms.DateInput):
    input_type = 'date' 
class PasswordInputField(forms.PasswordInput):
    input_type = 'password' 

class EmployeeSelectForm(forms.ModelForm):
    first_name = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    last_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    email_address = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control'}) )
    contact_no = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}) )
    password_1 = forms.CharField(label='',widget=PasswordInputField(attrs={'class':'form-control'}))
    password_2 = forms.CharField(label='',widget=PasswordInputField(attrs={'class':'form-control'}))
    
    date_of_birth = forms.DateField(label='',widget=DateInputField(attrs={'class': 'form-control'}) )
    date_employed = forms.DateField(label='',widget=DateInputField(attrs={'class': 'form-control'}) )
     

    class Meta:
        model = Employee
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(EmployeeSelectForm, self).__init__(*args, **kwargs)

        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['supervisor'].widget.attrs['class'] = 'form-control'
        self.fields['department'].label = ''
        self.fields['supervisor'].label = ''
    