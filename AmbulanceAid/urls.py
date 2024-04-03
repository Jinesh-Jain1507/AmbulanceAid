from django.contrib import admin
from django.urls import path
from core import views as cr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cr.Home),
    path('about/', cr.About, name='about'),
    path('contact/', cr.Contact, name='contact'),
    path('terms/', cr.Terms, name='terms'),
    path('privacy/', cr.Privacy, name='privacy'),
    path('logout/', cr.user_logout, name='logout'),
    path('login/', cr.Login, name='login'),
    path('register/<int:choice>/', cr.Register, name='register'),
    path('registerchoice/', cr.RegisterOption, name='registeroption'),
    path('dashboard/<int:id>/', cr.Dashboard, name='dashboard'),
    path('bookingdetails/<int:id>/', cr.ViewBooking, name='booking'),
    path('addhospital/', cr.Add_hospital, name='addhospital'),
    path('updatehospital/<int:id>/', cr.Update_hospital, name='updatehospital'),
    path('deletehospital/<int:id>/', cr.Delete_hospital, name='deletehospital'),
    path('viewhospital/<int:id>/', cr.View_hospital, name='viewhospital'),
    path('viewambulance/<int:id>/', cr.View_ambulance, name='viewambulance'),
    path('updateambulance/<int:id>/', cr.Update_ambulance, name='updateambulance'),
    path('deleteambulance/<int:id>/', cr.Delete_ambulance, name='deleteambulance'),
    path('addambulance/<int:id>/', cr.Add_ambulance, name='addambulance'),
    path('selectambulance/', cr.Ambulance_selection, name='selectambulance'),
    path('bookambulance/', cr.Ambulance_booking, name='bookambulance'),
    path('patientdetails/<int:id>', cr.Patient_details, name='patientdetails'),
    path('profile/', cr.Add_profile, name='profile'),
]
