from django.db import models
from django.utils import timezone
from blog.models import Car
import pycountry
class Booking(models.Model):
    

    COUNTRY_CHOICES = [(country.alpha_2, country.name) for country in pycountry.countries]


    INSURANCE_CHOICES = [
        ('basic', 'Basic'),
        ('full', 'Full'),  # Corrected to 'complicate'
    ]
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    nationality = models.CharField(max_length=20, choices=COUNTRY_CHOICES, default='AL')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default='johnsmith@gmail.com')
    phone_number = models.CharField(max_length=20)
    patent_number = models.CharField(max_length=50)
    insurance = models.CharField(max_length=10, choices=INSURANCE_CHOICES, default='basic')  
    period_start = models.DateField()
    period_end = models.DateField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.surname}'

class BusyDate(models.Model):
    car_id = models.IntegerField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"Car ID: {self.car_id}, Start Date: {self.start_date}, End Date: {self.end_date}"
