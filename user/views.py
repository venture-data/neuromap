from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model

User = get_user_model()  # This will use your custom user model

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        if email and password:
            try:
                # Ensure the User model is correctly used
                user = User.objects.get(email=email)

                # Authenticate and log in the user
                if user.check_password(password):
                    auth_login(request, user)
                    if user.is_admin or user.is_superuser:
                        return redirect('dashboard')  # Redirect to the dashboard or another protected view
                    else:
                        messages.error(request, 'Sorry, you are not authorized to access this page.')
                        return redirect('login')
                    return redirect('dashboard')  # Redirect to the dashboard or another protected view
                else:
                    messages.error(request, 'Invalid email or password.')
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Email and password are required.')

    return render(request, 'patients/login.html')


def logout(request):
    auth_logout(request)  # Log out the user
    return redirect('login')  # Redirect to the sign-in page

