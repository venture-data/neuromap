# patient/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('patients-add/', views.patients_add, name='patients_add'),
    path('patients-details/', views.patients_details, name='patients_details'),
    path('qeeg-recording-page/', views.qeeg_recording_page, name='qeeg_recording_page'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
    path('support/', views.support, name='support'),
]