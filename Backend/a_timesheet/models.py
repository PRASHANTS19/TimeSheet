from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Master(models.Model):
    timesheet_id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=False, blank=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'employee_id')

    def clean(self):
        if Master.objects.filter(date=self.date, employee_id=self.employee_id).exists():
            raise ValidationError('This date already has an entry for this employee.')