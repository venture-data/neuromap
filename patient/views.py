from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from patient.forms import PatientForm
from neuromap.utils import is_admin_or_superuser

def patients_add(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to access the dashboard.")
        return redirect('login')  # Replace 'login' with the name of your login URL
    
    if not is_admin_or_superuser(request.user):
        messages.error(request, "Warning! You cannot by pass the Dashboard")
        return redirect('login')  # Replace 'login' with the name of your login URL
    
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