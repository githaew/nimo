from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from employee.forms import EmployeeForm
from .forms import RegistrationForm
from .forms import NextofkinForm
from .models import Employee


# Create your views here.
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    # form = RegistrationForm()
    return render(request, 'employee_list.html',context)

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/employee_list/')
def employee_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_form.html',{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/employee/employee_list/')
def nextofkin(request):
    form = NextofkinForm()
    return render(request, 'nextofkin.html',{'form':form})