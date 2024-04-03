from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import User, Hospital, Ambulance, AmbulanceBooking, Departments, UserProfile, Diseases
from django.utils.translation import gettext, gettext_lazy as _

class HospitalReistrationForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['HospitalName', 'CurrentDirector', 'DirectorPhone', 'Address', 'Pincode', 'YearOfOpening', 'Contact', 'Email', 
                  'AmbulanceAvailable', 'Multispeciality', 'EmergencyOperation', 'BloodBank', 'ICU', 'Department']
        labels = {'HospitalName': 'Hospital Name', 'CurrentDirector': 'Director', 'DirectorPhone': 'Director Phone no.', 'Address': 'Address', 
                  'Pincode': 'Pincode', 'YearOfOpening': 'Year of Opening', 'Contact': 'Hospital Phone no.', 'Email': 'Hospital Email',
                  'AmbulanceAvailable': 'Are Ambulances Available?', 'Multispeciality': 'Is it a Multispeciality Hospital?', 
                  'EmergencyOperation': 'Has an Emergency Operation Theatre?', 'BloodBank': 'Has a Blood Bank?', 'ICU': 'Has an ICU?', 
                  'Department': 'Departments Available'}
    Department = forms.ModelMultipleChoiceField(queryset=Departments.objects.all(), widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        super(HospitalReistrationForm, self).__init__(*args, **kwargs)

        # Add 'form-control' class to all fields
        for field_name in self.fields:
            if not isinstance(self.fields[field_name].widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.RadioSelect)):
                self.fields[field_name].widget.attrs['class'] = 'form-control'

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'}),'email': forms.TextInput(attrs={'class': 'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['DateOfBirth', 'Address', 'Contact', 'BloodGroup', 'Disease']
        labels = {'DateOfBirth': 'Date of Birth', 'Address': 'Address', 'Contact': 'Phone no.', 
                  'BloodGroup': 'Blood Group', 'Disease': 'Past Diseases'}
    DateOfBirth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Disease = forms.ModelMultipleChoiceField(queryset=Diseases.objects.all(), widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Add 'form-control' class to all fields
        for field_name in self.fields:
            if not isinstance(self.fields[field_name].widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.RadioSelect)):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
    
class AmbulanceRegistrationForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['DriverName', 'DriverNumber', 'CarNumber', 'Experience', 'License', 'Type', 'DateOfBirth','Address']
        labels = {'DriverName': 'Driver Name', 'DriverNumber': 'Driver Phone No.', 'CarNumber': 'Ambulance Number', 
                  'Experience': 'Experience(in years)', 'Type': 'Select Ambulance Type', 'License': 'License No.', 
                  'DateOfBirth': 'Date Of Birth', 'Address': 'Address', 'License': 'License No.' }
    DateOfBirth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    def __init__(self, *args, **kwargs):
        super(AmbulanceRegistrationForm, self).__init__(*args, **kwargs)

        # Add 'form-control' class to all fields
        for field_name in self.fields:
            if not isinstance(self.fields[field_name].widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.RadioSelect)):
                self.fields[field_name].widget.attrs['class'] = 'form-control'

class AmbulanceSelectionForm(forms.ModelForm):
    locationpincode = forms.IntegerField(label='Location Pincode')
    class Meta:
        model = Ambulance
        fields = ['Type']
        labels = {'Type': 'Select Ambulance Type'}
    def __init__(self, *args, **kwargs):
        super(AmbulanceSelectionForm, self).__init__(*args, **kwargs)

        # Add 'form-control' class to all fields
        for field_name in self.fields:
            if not isinstance(self.fields[field_name].widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.RadioSelect)):
                self.fields[field_name].widget.attrs['class'] = 'form-control'
        
class AmbulanceBookingForm(forms.ModelForm):
    class Meta:
        model = AmbulanceBooking
        fields = ['PatientCondition', 'Address', 'Age', 'Gender', 'Injured', 'CurrentStatus']
        labels = {'PatientCondition': 'Current Condition of Patient', 'Address': 'Address', 'Age': 'Age of Patient', 'Gender': 'Gender of Patient', 'Injured': 'Are there more than 1 people injured?', 'CurrentStatus': 'Current status of patient'}
    def __init__(self, *args, **kwargs):
        super(AmbulanceBookingForm, self).__init__(*args, **kwargs)

        # Add 'form-control' class to all fields
        for field_name in self.fields:
            if not isinstance(self.fields[field_name].widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.RadioSelect)):
                self.fields[field_name].widget.attrs['class'] = 'form-control'