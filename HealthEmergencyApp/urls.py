"""
URL configuration for HealthEmergency project.

The `urlpatterns` lis    t routes URLs to views. For more information please see:
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
    path('ViewDoctor',ViewDoctor.as_view(),name="ViewDoctor"),
    path('AddBed',AddBed.as_view(),name="AddBed"),
    path('managebed',managebed.as_view(),name="managebed"),
    path('editdoctor/<int:id>',editdoctor.as_view(),name="editdoctor"),
    path('deletedoctor/<int:id>',deletedoctor.as_view(),name="deletedoctor"),
    path('deletebed/<int:id>',deletebed.as_view(),name="deletebed"),
    path('editbed/<int:id>',editbed.as_view(),name="editbed"),
    path('add_manage_prescription',AddManagePrescription.as_view(),name="AddManagePrescription"),
    path('AddPrescription',AddPrescription.as_view(),name="AddPrescription"),


    #////////////////////////////////////////// PHARMACY ////////////////////////////////////////

    path('', LoginPage.as_view(), name="LoginPage"),
    path('Register_phmy',Register_phmy.as_view(),name="Register"),
    path('Homepage_phmy',Homepage_phmy.as_view(),name="Homepage"),
    path('PharmacyEquipments',PharmacyEquipments.as_view(),name="PharmacyEquipments"),
    path('ManageBooking',ManageBooking.as_view(),name="ManageBooking"),
    path('addequipment',addequipment.as_view(),name='addequipment'),
    path('Accept_B/<int:id>',AcceptBooking.as_view(),name="AcceptPharmacy"),
    path('Reject_B/<int:id>',RejectBooking.as_view(),name="RejectPharmacy"),

    #######################################################################################

    path('User_Registration',UserReg_api.as_view(),name='User_Registration'),
    path('User_Login',LoginPage_api.as_view(),name='User_Login'),
    path('Hospital_view',ViewHospitalAPI.as_view(),name="Hospital_view"),
    path('Doctor_view/<int:id>',ViewDoctorAPI.as_view(),name="Doctor_view"),
    path('Doctor_book/<int:id>',BookDoctorApi.as_view(),name='BookDoctorApi'),
    path('ambulance_view/<int:hospital_id>',AmbulanceByHospitalAPI.as_view(),name="Ambulance_view"),
    path('ambulancebooking_history/<int:lid>',AmbulanceBookingHistoryAPI.as_view(),name="AmbulanceBooking_history"),
    path('ambulancebooking/<int:lid>/<int:ambulance_id>',AmbulancebookingAPI.as_view(),name="AmbulanceBooking"),
    path('bedbooking/<int:id>',BedBookingAPI.as_view(),name="BedBooking"),
    path('view_bed/<int:id>',ViewBedAPI.as_view(),name="View_Bed"),
    path('bedbooking_history/<int:id>',BedBookingHistoryAPI.as_view(),name="BedBooking_history"),
    path("doctor_booking_history/<int:id>", BookingHis.as_view(), name="doctor_booking_history"),

    
    
    


]   


