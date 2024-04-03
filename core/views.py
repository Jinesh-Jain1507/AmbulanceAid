from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm, SignupForm, HospitalReistrationForm, AmbulanceBookingForm, AmbulanceRegistrationForm, AmbulanceSelectionForm, UserProfileForm
from .models import User, Hospital, Ambulance, AmbulanceBooking, CustomSession, UserProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model

# Create your views here.

#Home
def Home(request):
    if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                id = user.id
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return HttpResponseRedirect('/dashboard/%s' %id)
    else:
        form = LoginForm()
        return render(request, 'core/home.html', {'form': form})

#About
def About(request):
    return render(request, 'core/about.html')

#Terms
def Terms(request):
    return render(request, 'core/terms.html')

#Privacy
def Privacy(request):
    return render(request, 'core/privacy.html')

#Contact
def Contact(request):
    return render(request, 'core/contact.html')

#Dashboard
def Dashboard(request, id):
    if request.user.is_authenticated:
        if id == request.user.id:
            role = get_user_model().objects.get(pk=id).role
            full_name = request.user.get_full_name
            if role:
                hospitals = Hospital.objects.filter(Admin = id)
                return render(request, 'core/hospitaldashboard.html', {'full_name': full_name, 'hospitals': hospitals})
            else:
                bookings = AmbulanceBooking.objects.filter(Customer = id)
                profile = UserProfile.objects.filter(User = id)
                diseases = None
                if profile:
                    profile = UserProfile.objects.filter(User = id)[0]
                    if profile.Diseases:
                        diseases = profile.Diseases.all()
                return render(request, 'core/userdashboard.html', {'full_name': full_name, 'bookings': bookings, 'profile': profile, 'diseases': diseases})
        else:
            messages.error(request, "Forbidden Action")
            return HttpResponseRedirect('/') 
    else:
        return HttpResponseRedirect('/login/')
    
#View Booking Details
def ViewBooking(request, id):
    booking = AmbulanceBooking.objects.get(pk=id)
    if booking.Customer == request.user:
        return render(request, 'core/bookingdetails.html', {'booking': booking})
    else:
        messages.error(request, "Forbidden Action")
        return HttpResponseRedirect('/')

#Registration Choice
def RegisterOption(request):
    return render(request, 'core/registeroption.html')

#Register
def Register(request, choice):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if choice == 1:
                role = False
            elif choice == 2:
                role = True
            messages.success(request, "Congratulations! Registration Successful")
            instance = form.save(commit=False)
            instance.role = role
            instance.save()
            form = SignupForm()
            return HttpResponseRedirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form':form})


#Login
def Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                id = user.id
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return HttpResponseRedirect('/dashboard/%s' %id)
        else:
            form = LoginForm()
        return render(request, 'core/login.html', {'form': form})
    else:
        id = user.id
        return HttpResponseRedirect('/dashboard/%s' %id)

#Logout
def user_logout(request):
    logout(request)
    messages.error(request, "Logged Out")
    return HttpResponseRedirect('/')

#Add Profile
def Add_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =UserProfileForm(request.POST)
            if form.is_valid():
                form.instance.User = request.user
                form.save()
                messages.success(request, "Updated Successfully")
                return HttpResponseRedirect('/dashboard/%s' %request.user.id)
        else:
            form = UserProfileForm()
        return render(request, 'core/profile.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

#Add Hospital
def Add_hospital(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HospitalReistrationForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.Admin = request.user
                instance.save()
                messages.success(request, "Added Successfully")
                return HttpResponseRedirect('/dashboard/%s' %request.user.id)
        else:
            form = HospitalReistrationForm()
        return render(request, 'core/addhospital.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')
    
#View Hospital
def View_hospital(request, id):
        hospital = Hospital.objects.get(pk=id)
        id = hospital.id
        ambulances = Ambulance.objects.filter(Hospital = id)
        department = hospital.Department.all()
        return render(request, 'core/viewhospital.html', {'hospital': hospital, 'ambulances': ambulances, 'department': department})

#View Ambulance
def View_ambulance(request, id):
        hospital = Hospital.objects.get(pk=id)
        id = hospital.id
        ambulances = Ambulance.objects.filter(Hospital = id)
        department = hospital.Department.all()
        return render(request, 'core/viewambulance.html', {'hospital': hospital, 'ambulances': ambulances, 'department': department})

#Update Hospital
def Update_hospital(request, id):
    if request.user.is_authenticated:
        pi = Hospital.objects.get(pk=id)
        if pi.Admin == request.user:    
            if request.method == 'POST':
                pi = Hospital.objects.get(pk=id)
                form = HospitalReistrationForm(request.POST, instance=pi)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Updated Successfully")
                    return HttpResponseRedirect('/dashboard/%s' %request.user.id)
            else:
                pi = Hospital.objects.get(pk=id)
                form = HospitalReistrationForm(instance=pi)
            return render(request, 'core/updatehospital.html', {'form': form})
        else:
            messages.error(request, "Forbidden Action")
            return HttpResponseRedirect('/')    
    else:
        return HttpResponseRedirect('/login/')

#Delete Hospital
def Delete_hospital(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Hospital.objects.get(pk=id)
            pi.delete()
            id = request.user.id
            return HttpResponseRedirect('/dashboard/%s' %id)
        else:
            messages.error(request, "Forbidden Action")
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')
    
#Add Ambulance
def Add_ambulance(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AmbulanceRegistrationForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.Hospital = Hospital.objects.get(pk=id)
                instance.save()
                messages.success(request, "Added Successfully")
                return HttpResponseRedirect('/viewhospital/%s' %id)
        else:
            form = AmbulanceRegistrationForm()
        return render(request, 'core/addambulance.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')
    
#Update Ambulance
def Update_ambulance(request, id):
    if request.user.is_authenticated:
        pi = Ambulance.objects.get(pk=id)
        if pi.Hospital.Admin == request.user:    
            if request.method == 'POST':
                pi = Ambulance.objects.get(pk=id)
                form = AmbulanceRegistrationForm(request.POST, instance=pi)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Updated Successfully")
                    return HttpResponseRedirect('/viewhospital/%s' %pi.Hospital.id)
            else:
                pi = Ambulance.objects.get(pk=id)
                form = AmbulanceRegistrationForm(instance=pi)
            return render(request, 'core/updateambulance.html', {'form': form})
        else:
            messages.error(request, "Forbidden Action")
            return HttpResponseRedirect('/')    
    else:
        return HttpResponseRedirect('/login/')
    
#Delete Ambulance
def Delete_ambulance(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Ambulance.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/viewhospital/%s' %pi.Hospital.id)
        else:
            messages.error(request, "Forbidden Action")
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')
    
#Ambulance Selection
def Ambulance_selection(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AmbulanceSelectionForm(request.POST)
            if form.is_valid():
                pin = form.cleaned_data['locationpincode']
                ambulancetype = form.cleaned_data['Type']
                hospital = Hospital.objects.filter(Pincode=pin)
                for i in range(0, len(hospital)):
                    ambulance = Ambulance.objects.filter(Hospital=hospital[i])
                    for j in range(0, len(ambulance)):
                        if ambulance[j].Available:
                            if ambulance[j].Type == ambulancetype:
                                CustomSession.objects.create(Ambulanceid=ambulance[j])                  
                return HttpResponseRedirect('/bookambulance/')
        else:
            cache = CustomSession.objects.all()
            cache.delete()
            form = AmbulanceSelectionForm()
            return render(request, 'core/ambulanceselection.html', {'form': form})
            
    else:
        return HttpResponseRedirect('/login/')
    
#Book Ambulance
def Ambulance_booking(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Ambulance.objects.get(pk=id).id
            return HttpResponseRedirect(request, '/patientdetails/%s' %pi)
        else:
            ambulances = CustomSession.objects.all()
            return render(request, 'core/bookambulance.html', {'ambulances': ambulances})
    else:
        return HttpResponseRedirect('/login/')

def Patient_details(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AmbulanceBookingForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.Ambulance = Ambulance.objects.get(pk=id)
                instance.Customer = request.user
                instance.save()
                pi = Ambulance.objects.get(pk=id)
                pi.Available = False
                pi.save()
                messages.success(request, "Booked Successfully")
                return HttpResponseRedirect('/dashboard/%s' %request.user.id)
        else:
            form = AmbulanceBookingForm()
        return render(request, 'core/patientdetails.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')