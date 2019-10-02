from django.contrib import admin
from .models import Employee
class EmployeeAdmin(admin.ModelAdmin):
  list_display=['id']

admin.site.register(Employee)
