from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator




class Employee(models.Model):
    
    CONTRACT_TYPE_CHOICES = [
        ('permanent', 'Permanent'),
        ('fixed-term', 'Fixed-term'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    DEPARTMENT_CHOICES = [
        ('hr', 'Human Resources'),
        ('it', 'Information Technology'),
        ('sales', 'Sales'),
        ('finance', 'Finance'),
        ('marketing', 'Marketing'),
    ]

    name_validator = RegexValidator(r'^[a-zA-Z]+$', 'Only letters are allowed.')

    first_name = models.CharField(max_length=50, validators=[name_validator])
    last_name = models.CharField(max_length=50, validators=[name_validator])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)  
    birth_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)], null=False, blank=False)
    start_date = models.DateField()
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPE_CHOICES)  
    contract_duration = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES) 
    
    annual_leave_days = models.IntegerField(null=True, blank=True, default=None)
    free_days = models.IntegerField(null=True, blank=True, default=None)
    paid_leave_days = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
   
