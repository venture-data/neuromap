from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
