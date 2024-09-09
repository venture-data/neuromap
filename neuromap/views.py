from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import is_admin_or_superuser

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if not is_admin_or_superuser(request.user):
        messages.error(request, "Warning! You cannot by pass the Dashboard")
        return redirect('login')
    
    return render(request, 'patients/index.html')