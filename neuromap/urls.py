"""
URL configuration for foodapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.login, name='login'),
    path('dashboard/', views.index, name='dashboard'),
    path('patients-add/', views.patients_add, name='patients_add'),
    path('patients-details/', views.patients_details, name='patients_details'),
    path('qeeg-recording-page/', views.qeeg_recording_page, name='qeeg_recording_page'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
    path('support/', views.support, name='support'),
]


