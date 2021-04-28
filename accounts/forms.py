from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name',
            'last_name', 'email',
            'password1', 'password2',
        ]


class DriverInfoForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            'reg_No',
        ]


class CustomerEditForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'phone', 'address', 'town',
            'county', 'postcode', 'payment_method',
        ]


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class TripBookingForm(forms.ModelForm):

    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Booking
        fields = [

            'start_address', 'destination_address',
            'date', 'time',
        ]