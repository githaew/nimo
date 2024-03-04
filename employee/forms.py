from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registration
from .models import Nextofkin

from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fullname', 'email', 'emp_code', 'mobile_no', 'position']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['firstname', 'lastname', 'phone_no', 'password']
class NextofkinForm(forms.ModelForm):
    class Meta:
        model = Nextofkin
        fields = ['fullname', 'employee_name', 'phone_no', 'id_no']