from django.db import models



from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.db import models
import re

class Student(models.Model):
    first_name = models.CharField(
        max_length=30,
        validators=[RegexValidator(r'^[A-Za-z]+$', 'First name must contain only letters.')]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[RegexValidator(r'^[A-Za-z]+$', 'Last name must contain only letters.')]
    )
    stream = models.CharField(
        max_length=50,
        validators=[RegexValidator(r'^[A-Za-z\s]+$', 'Stream must contain only letters and spaces.')]
    )
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator('Enter a valid email address.')]
    )
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10}$', 'Phone number must be exactly 10 digits.')]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        # Additional validation logic can go here if needed
        # Example: prevent duplicate phone numbers (not enforced by unique=True)
        if Student.objects.exclude(pk=self.pk).filter(phone=self.phone).exists():
            raise ValidationError({'phone': 'This phone number is already registered.'})

# class Student(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     stream = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# Create your models here.


