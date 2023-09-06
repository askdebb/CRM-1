from django.db import models
from django.conf import settings

# Create your models here.


class Department(models.Model):
    name = models.CharField("Department name", max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Department"
    
class Supervisor(models.Model):
    first_name = models.CharField("Supervisor's First name", max_length=50, null=True, blank=True)
    last_name = models.CharField("Supervisor's Last name", max_length=50, null=True, blank=True)
    email_address = models.CharField("Supervisor's Email Address", max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=False, blank=False, default='')
    department = models.OneToOneField("Department", Department, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = "Supervisor"
    

class Inventory(models.Model):
    name = models.CharField("Inventory name", max_length=50 , null=True , blank=True)
    description = models.TextField("Inventory Description", null=True, blank=True)
    procured_date = models.DateTimeField("Inventory Date Bought", auto_now_add=True, null=False, blank=False)
    date_maintained = models.DateTimeField("Inventory Date Maintained",auto_now_add=True, null=True, blank=True)
    price = models.CharField("Inventory price",max_length=10, null=False, blank=False)
    supervisor_responsible = models.OneToOneField(Supervisor , on_delete=models.SET_NULL, null=True)
    departments_to_use = models.ManyToManyField(Department)
    
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Inventory"
    

class Employee(models.Model):
    first_name = models.CharField("First Name", max_length=60, blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=60, blank=True, null=True)
    email_address = models.EmailField("Email Address", max_length=60, blank=True, null=True)
    contact_no = models.CharField("Contact Number", max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=False, blank=False, default='')
    date_employed = models.DateField("Date Employed", default='', null=False, blank=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="employee_department")
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True,  related_name="employee_supervisor")
    
    
    def __str__(self):
        return self.first_name 
    
    class Meta:
        verbose_name_plural = "Employee"
    
# class DepartmentsInvolved(models.Model):
#     departments_to_use = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
#     inventory_to_be_used = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True)


    
