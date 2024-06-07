from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages



def home(request):
    context = {
        "employees": Employee.objects.all()


    }
    return render (request, "employee/home.html", context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee has been added successfully!')
            return redirect('employee-home') 
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee has been updated successfully!')
            return redirect('employee-home') 
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/update_employee.html', {'form': form, 'employee': employee})

def detail_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee/detail_employee.html', {'employee': employee})