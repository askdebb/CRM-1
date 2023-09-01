from django.contrib import admin
from .models import Department, Supervisor, Employee, Inventory

# Register your models here.


admin.site.register(Department)
# admin.site.register(Supervisor)
# admin.site.register(Employee)
# admin.site.register(Inventory)


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name'), ('email_address','date_of_birth'), 'department']
    list_display = ('first_name', 'email_address', 'department')
    
    
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    # fields = (('name', 'last_name'), ('email_address','date_of_birth'), 'department')
    list_display = ('name', 'supervisor_responsible',  'price')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # fields = (('name', 'last_name'), ('email_address','date_of_birth'), 'department')
    list_display = ('first_name', 'date_employed', 'department', 'supervisor')