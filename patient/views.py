from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from patient.models import Patient
from neuromap.utils import is_admin_or_superuser
from datetime import datetime

def patients_add(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to access the dashboard.")
        return redirect('login')  # Replace 'login' with the name of your login URL
    
    if not is_admin_or_superuser(request.user):
        messages.error(request, "Warning! You cannot by pass the Dashboard")
        return redirect('login')  # Replace 'login' with the name of your login URL
    
    if request.method == 'POST':
        # Get the data from the form
        name = request.POST.get('name')
        dob_str = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        clinic_id = request.POST.get('clinic_id')
        contact_name = request.POST.get('contact_name')
        contact_mobile = request.POST.get('contact_mobile')
        notes_by_admin = request.POST.get('notes_by_admin', '')
        notes_by_neuroscientist = request.POST.get('notes_by_neuroscientist', '')

        # Convert the DOB string from 'dd/mm/yyyy' to 'yyyy-mm-dd'
        try:
            dob = datetime.strptime(dob_str, '%d/%m/%Y').strftime('%Y-%m-%d')  # Convert to 'yyyy-mm-dd'
        except ValueError:
            # Handle invalid date format
            return render(request, 'patients/patients-add.html', {
                'error': 'Invalid date format. Please use DD/MM/YYYY.',
                'form_data': request.POST
            })

        # Create a new Patient instance and save it
        new_patient = Patient(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            clinic_id=clinic_id,
            contact_name=contact_name,
            contact_mobile=contact_mobile,
            notes_by_admin=notes_by_admin,
            notes_by_neuroscientist=notes_by_neuroscientist
        )
        new_patient.save()

        messages.success(request, 'Patient Successfully Added')
        return redirect('patients_add')

    return render(request, 'patients/patients-add.html')

def patients_all(request):
    return render(request, 'patients/patients.html')

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