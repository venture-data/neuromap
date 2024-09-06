from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import User 
from django.shortcuts import render, redirect
from patient.forms import PatientForm

def index(request):
    return render(request, 'patients/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if email and password:
            try:
                user = User.objects.get(email=email.lower())
                if user:
                    print("user found")
                    return redirect('dashboard')
                print(user)
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Email and password are required.')

    return render(request, 'patients/login.html')

def patients_add(request):
    print( request.POST)
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # Save the new patient to the database
            form.save()
            messages.success(request, 'Patient added successfully.')
            return redirect('patients_add')
        else:
            messages.error(request, 'There was an error adding the patient. Please check the form.')
    else:
        form = PatientForm()

    return render(request, 'patients/patients-add.html', {'form': form})

def patients_details(request):
    return render(request, 'patients/patients-details.html')

def qeeg_recording_page(request):
    return render(request, 'patients/qeeg-recording-page.html')

def reports(request):
    return render(request, 'patients/reports.html')

def settings(request):
    return render(request, 'patients/settings.html')

def support(request):
    return render(request, 'patients/support.html')
