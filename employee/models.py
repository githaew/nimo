from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    emp_code = models.CharField(max_length=5)
    mobile_no = models.CharField(max_length=15)
    position = models.CharField(max_length=20)
    def __str__(self):
        return self.fullname

class Registration(models.Model):
    firstname = models.CharField(max_length=12)
    lastname = models.CharField(max_length=12)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=6)
    def __str__(self):
        return self.lastname
class Nextofkin(models.Model):
    fullname = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    id_no = models.CharField(max_length=14)
    phone_no = models.CharField(max_length=15)
    def __str__(self):
        return self.id_no
