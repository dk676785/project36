from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Employee

class ViewAllEmployees(ListView):
    template_name = 'viewall.html'
    model = Employee


class ViewAllEmployeesSalaryId(ListView):
    template_name = 'viewallsalid.html'
    model = Employee
    queryset = Employee.objects.values('salary','idno')


class ViewAllEmployeeNames(ListView):
    template_name = 'viewnames.html'
    model = Employee
    queryset = Employee.objects.values('name')


class AllEmployeeIds(ListView):
    template_name = 'allids.html'
    model = Employee
    queryset = Employee.objects.values('idno')

class OneEmployee(DetailView):
    template_name = "oneemp.html"
    model = Employee