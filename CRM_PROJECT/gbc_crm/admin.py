from django.contrib import admin
from .models import Department, Supervisor, Employee, Inventory

# Register your models here.


admin.site.register(Department)
admin.site.register(Supervisor)
admin.site.register(Employee)
admin.site.register(Inventory)
