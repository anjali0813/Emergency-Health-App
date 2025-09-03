"""
URL configuration for HealthEmergency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from HealthEmergencyApp.views import *


urlpatterns = [
    # ///////////////////////////////////////// ADMIN ////////////////////////////////////////////
    path('', LoginPage.as_view(), name="LoginPage"),
    path('Homepage',Homepage.as_view(),name="Homepage"),
    path('ComplaintReply',ComplaintReply.as_view(),name="ComplaintReply"),
    path('Reply/<int:id>',Reply.as_view(),name="Reply"),
    path('VerifyHospital',VerifyHospital.as_view(),name="VerifyHospital"),
    path('ViewUsers',ViewUsers.as_view(),name="ViewUsers"),
    path('Accept_H/<int:id>',AcceptHospital.as_view(),name="AcceptHospital"),
    path('Reject_H/<int:id>',RejectHospital.as_view(),name="RejectHospital"),
    path('VerifyPharmacy',VerifyPharmacy.as_view(),name="VerifyPharmacy"),
    path('Accept_P/<int:id>',AcceptPharmacy.as_view(),name="AcceptPharmacy"),
    path('Reject_P/<int:id>',RejectPharmacy.as_view(),name="RejectPharmacy"),
    path('TravelFacility',TravelFacility.as_view(),name="TravelFacility"),
    path('Vehicle',Vehicle.as_view(),name="Vehicle"),
    # ////////////////////////////////////// HOSPITAL /////////////////////////////////////////////////
    path('Homepage_hsptl',Homepage_hsptl.as_view(),name="Homepage"),
    path('Register_hsptl',Register_hsptl.as_view(),name="Register"),
    path('ManageAppointment',ManageAppointment.as_view(),name="ManageAppointments"),
    path('ReviewRate',ReviewRate.as_view(),name="ReviewRate"),
    path('AddManageDoctors',AddManageDoctors.as_view(),name="AddManageDoctors"),
    path('AddBed',AddBed.as_view(),name="AddBed"),
    #////////////////////////////////////////// PHARMACY ////////////////////////////////////////
    path('Register_phmy',Register_phmy.as_view(),name="Register"),
    path('Homepage_phmy',Homepage_phmy.as_view(),name="Homepage"),
    path('PharmacyEquipments',PharmacyEquipments.as_view(),name="PharmacyEquipments"),
    path('ManageBooking',ManageBooking.as_view(),name="ManageBooking"),

    

]


