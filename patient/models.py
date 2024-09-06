from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    clinic_id = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_mobile = models.CharField(max_length=15)
    notes_by_admin = models.TextField(blank=True, null=True)
    notes_by_neuroscientist = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
