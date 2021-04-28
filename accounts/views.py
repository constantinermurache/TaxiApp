from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render

from .decorators import *
from .forms import *


def home(request):
    return render(request, 'accounts/dashboard.html')


@unauthenticated_user
def customer_register(request):  # is going to be a customer registration page
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='CUSTOMER')
            user.groups.add(group)
            Customer.objects.create(customer=user, )

            messages.success(request, 'Account was created for ' + username)
            return redirect('loginPage')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def register_type(request):
    return render(request, 'accounts/signupType.html')


@unauthenticated_user
def driver_register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='DRIVER')
            user.groups.add(group)
            Driver.objects.create(driver=user, )
            messages.success(request, 'Account was created for ' + username)
            return redirect('loginPage')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('homePage')


# lists the logged-in user bookings
@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['CUSTOMER'])
def user_page(request):
    bookings = request.user.customer.booking_set.all()

    pending = bookings.filter(status='Pending').count()
    in_progress = bookings.filter(status='In Progress').count()
    finished = bookings.filter(status='Finished').count()

    context = {'bookings': bookings, 'pending': pending,
               'in_progress': in_progress, 'finished': finished}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['CUSTOMER'])
def booking_view(request):
    if request.method == 'POST':
        form = TripBookingForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.customer = request.user.customer  # logged-in User
            trip.save()
            return redirect('userBookingsList')
    else:
        form = TripBookingForm()
    context = {'form': form}
    return render(request, 'accounts/booking_form.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['CUSTOMER'])
def update_booking_view(request, pk):
    booking = Booking.objects.get(id=pk)

    if request.method == 'POST':
        form = TripBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('userBookingsList')
    else:
        form = TripBookingForm(instance=booking)
    context = {'form': form}
    return render(request, 'accounts/booking_form.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['CUSTOMER'])
def customer_delete_booking_view(request, pk):
    booking = Booking.objects.get(id=pk)

    if request.method == 'POST':
        booking.delete()
        return redirect('userBookingsList')
    context = {'booking': booking}
    return render(request, 'accounts/customer_delete_booking.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['CUSTOMER'])
def edit_customer_profile(request):
    if request.method == 'POST':
        form = CustomerEditForm(request.POST, instance=request.user.customer)
        if form.is_valid():
            form.save()
            messages.success(request, f'The user information has been updated successfully')
            return redirect('homePage')
    else:
        form = CustomerEditForm(instance=request.user.customer)
    context = {'form': form}
    return render(request, 'accounts/edit_customer_profile.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['DRIVER'])
def edit_driver_profile(request):
    if request.method == 'POST':
        form = DriverInfoForm(request.POST, instance=request.user.driver)
        if form.is_valid():
            form.save()
            messages.success(request, f'The user information has been updated successfully')
            return redirect('homePage')
    else:
        form = DriverInfoForm(instance=request.user.driver)
    context = {'form': form}
    return render(request, 'accounts/edit_customer_profile.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['DRIVER'])
def available_trips(request):
    bookings_pending = Booking.objects.filter(status='Pending').all()
    driver = request.user.driver
    bookings_in_progress = Booking.objects.filter(status='In Progress', driver=driver).all()
    bookings_finished = Booking.objects.filter(status='Finished', driver=driver).all()

    context = {'bookings_pending': bookings_pending,
               'bookings_in_progress': bookings_in_progress,
               'bookings_finished': bookings_finished}
    return render(request, 'accounts/available_trip_driver.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['DRIVER'])
def accept_booking_driver(request, pk):
    booking = Booking.objects.get(id=pk)
    driver = request.user.driver
    if request.method == 'POST':
        booking.driver = driver
        booking.status = 'In Progress'
        booking.save()
        return redirect('driverTrips')

    context = {'booking': booking}
    return render(request, 'accounts/accept_booking_driver.html', context)


@login_required(login_url='loginPage')
@allowed_user(allowed_roles=['DRIVER'])
def cancel_booking_driver(request, pk):
    booking = Booking.objects.get(id=pk)
    cancel = None
    if request.method == 'POST':
        booking.driver = cancel
        booking.status = 'Pending'
        booking.save()
        return redirect('driverTrips')
    context = {'booking': booking}
    return render(request, 'accounts/cancel_booking_driver.html', context)




