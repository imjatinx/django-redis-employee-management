from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Department(models.Model):
    name = models.CharField(_("name"), max_length=50)
    location = models.CharField(_("location"), max_length=100)
    employees = models.ManyToManyField("Employee", null=True, blank=True, related_name='employee_name')

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), unique=True)
    phone_number = models.CharField(_("phone number"), max_length=20)
    department = models.ForeignKey("Department", null=True, blank=True, on_delete=models.CASCADE)
    hire_date = models.DateField(_("hire date"))
    salary = models.DecimalField(_("salary"), max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

