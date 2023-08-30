from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField("Department name", max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Supervisor(models.Model):
    name = models.CharField("Supervisor's name", max_length=50, null=True, blank=True)
    department = models.OneToOneField("Department", Department, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Inventory(models.Model):
    name = models.CharField("Inventory name", max_length=50 , null=True , blank=True)
    description = models.TextField("Inventory Description", null=True, blank=True)
    procured_date = models.DateTimeField("Inventory Date Bought", null=False, blank=False)
    date_maintained = models.DateTimeField("Inventory Date Maintained", null=True, blank=True)
    price = models.CharField("Inventory price",max_length=10, null=False, blank=False)
    supervisor_responsible = models.OneToOneField(Supervisor , on_delete=models.SET_NULL, null=True)
    departments_to_use = models.ManyToManyField(Department, through="DepartmentsInvolved")
    
    
    
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name = models.CharField("Employee Name", max_length=60, blank=True, null=True)
    age = models.CharField("Employee's Age", max_length=2, null=True, blank=True)
    date_employed = models.DateField("Date Employed", default='', null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    supervisor = models.OneToOneField(Supervisor, on_delete=models.SET_NULL, null=True)
        
    
    
    def __str__(self):
        return self.name
    
class DepartmentsInvolved(models.Model):
    departments_to_use = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    inventory_to_be_used = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True)


    
