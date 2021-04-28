from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20, default='Your Phone')
    address = models.CharField(max_length=200,  default='Your Address')
    town = models.CharField(max_length=200,  default='Your Town')
    county = models.CharField(max_length=200,  default='Your County')
    postcode = models.CharField(max_length=20,  default='Your Postcode')
    payment_method = models.CharField(max_length=20,  default='Your Payment Method')

    def __str__(self):
        return f'{self.customer.username} Profile'


class Driver(models.Model):
    driver = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reg_No = models.CharField(max_length=20,  default='Your Registration Plate')
    availability = models.BooleanField('Available', default=True)

    def __str__(self):
        return self.driver.username


class Booking(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Finished', 'Finished'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL)
    date_booked = models.DateTimeField(auto_now_add=True, null=True)
    start_address = models.CharField(max_length=200, null=True)
    destination_address = models.CharField(max_length=200, null=True)
    date = models.DateField('Trip Date', null=True)
    time = models.TimeField('Trip Time', null=True)
    status = models.CharField(max_length=15, choices=STATUS, null=True, default='Pending')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "Booking "+str(self.id)

    def get_absolute_url(self):
        return reverse('userPage')





