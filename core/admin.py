from django.contrib import admin
from .models import User, Hospital, Ambulance, AmbulanceBooking, CustomSession, UserProfile, Diseases, Departments

# Register your models here.

@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'DateOfBirth', 'Address', 'Contact', 'BloodGroup']

@admin.register(Departments)
class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'department']

@admin.register(Diseases)
class DiseaseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'disease']

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'role']


@admin.register(Hospital)
class HospitalModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'HospitalName', 'CurrentDirector', 'Address', 'Pincode', 'YearOfOpening']

@admin.register(Ambulance)
class AmbulanceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'DriverName', 'DriverNumber', 'CarNumber', 'Type']

@admin.register(AmbulanceBooking)
class AmbulanceBookingModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'PatientCondition', 'Age', 'Gender', 'Injured', 'CurrentStatus', 'Status']

@admin.register(CustomSession)
class CustomSessionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Ambulanceid']

