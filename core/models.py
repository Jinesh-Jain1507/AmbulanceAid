from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime

# Create your models here.

class User(AbstractUser):
    role = models.BooleanField(default=False)

class Diseases(models.Model):
    disease = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.disease

class UserProfile(models.Model):
    User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    DateOfBirth = models.DateField()
    Address= models.CharField(max_length=250)
    Contact = models.IntegerField()
    BloodGroups = [('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')]
    BloodGroup = models.CharField(max_length=3, choices=BloodGroups)
    Diseases = models.ManyToManyField(Diseases)

class Departments(models.Model):
    department = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.department

class Hospital(models.Model):
    Admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    HospitalName= models.CharField(max_length=100)
    CurrentDirector= models.CharField(max_length=50)
    DirectorPhone = models.IntegerField()
    Address= models.CharField(max_length=250)
    Pincode= models.IntegerField()
    YearOfOpening= models.IntegerField()
    Contact = models.IntegerField()
    Email = models.EmailField()
    AmbulanceAvailable= models.BooleanField()
    Multispeciality= models.BooleanField()
    EmergencyOperation= models.BooleanField()
    BloodBank= models.BooleanField()
    ICU= models.BooleanField()
    Department = models.ManyToManyField(Departments)

class Ambulance(models.Model):
    Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    DriverName = models.CharField(max_length=100)
    DriverNumber = models.IntegerField()
    CarNumber = models.CharField(max_length=15)
    Experience = models.IntegerField()
    Types = [('T', 'Type 1'), ('C', 'Critical Care Transport'), ('D', 'Disaster Response'), ('S', 'Special Event Ambulance')]
    Type = models.CharField(max_length=1, choices=Types)
    License = models.CharField(max_length=15)
    DateOfBirth = models.DateField()
    Address= models.CharField(max_length=250)
    Available = models.BooleanField(default=True)


class AmbulanceBooking(models.Model):
    Ambulance = models.ForeignKey(Ambulance, on_delete=models.CASCADE)
    Customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Condition = [('C', 'Critical/Serious'), ('W', 'Can Wait'), ('U', 'Unknown')]
    PatientCondition = models.CharField(max_length=1, choices=Condition)
    Address= models.CharField(max_length=250)
    Age = models.IntegerField()
    gender = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    Gender = models.CharField(max_length=1,choices=gender)
    Injured = models.BooleanField()
    conditions = [('A', 'Accident/Severe Injuries'), ('B', 'Bleeding'), ('C', 'Childbirth/Delivery Emergencies'), ('D', 'Difficulty Breathing'),
                  ('H', 'Heart attack/ Stroke'), ('M', 'Altered Mental State'), ('P', 'Problem in Speaking or Swallowing'),
                  ('R', 'Severe Allergic Reaction'), ('S', 'Seizures'), ('U', 'Uncontrolled Pain'), ('F', 'UNKNOWN/found unconsious')]
    CurrentStatus = models.CharField(max_length=1, choices=conditions)
    DateTime = models.DateTimeField(default=datetime.datetime.now())
    status = [('B', 'Booked'), ('O', 'On the Way'), ('C', 'Completed')]
    Status = models.CharField(max_length=1, choices=status, default='B')

class CustomSession(models.Model):
    Ambulanceid = models.ForeignKey(Ambulance, on_delete=models.CASCADE)