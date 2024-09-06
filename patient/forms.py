from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'dob', 'age', 'gender', 'clinic_id', 'contact_name', 'contact_mobile', 'notes_by_admin', 'notes_by_neuroscientist']
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'DOB'}),
            'notes_by_admin': forms.Textarea(attrs={'placeholder': 'Notes by Admin'}),
            'notes_by_neuroscientist': forms.Textarea(attrs={'placeholder': 'Notes by Neuroscientist'}),
        }
