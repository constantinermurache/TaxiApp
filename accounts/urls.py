from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('register/', views.register_type, name='registerType'),
    path('register/customerRegister/', views.customer_register, name='customerRegister'),
    path('register/driverRegister/', views.driver_register, name='driverRegister'),
    path('login/', views.login_page, name='loginPage'),
    path('logout/', views.logout_user, name='logout'),
    path('user/', views.user_page, name='userBookingsList'),  # list the user bookings
    path('driver_trips/', views.available_trips, name='driverTrips'),  # list the  bookings for driver
    path('booking/', views.booking_view, name='tripBooking'),  # book a trip
    path('update_booking/<str:pk>/', views.update_booking_view, name='updateBooking'),  # update a booking
    path('delete_booking/<str:pk>/', views.customer_delete_booking_view, name='deleteBooking'),  # delete a booking
    path('accept_booking/<str:pk>/', views.accept_booking_driver, name='acceptBookingDriver'),  # accept a booking by driver
    path('cancel_booking/<str:pk>/', views.cancel_booking_driver, name='cancelBookingDriver'),  # cancel a booking by driver
    path('customer_details/', views.edit_customer_profile, name='customerDetails'),
    path('driver_details/', views.edit_driver_profile, name='driverDetails'),
]