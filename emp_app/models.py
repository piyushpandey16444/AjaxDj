from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)


class Employee(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    gender = models.CharField(max_length=50, choices=GENDER)
    office = models.ForeignKey("emp_app.Office", on_delete=models.CASCADE)