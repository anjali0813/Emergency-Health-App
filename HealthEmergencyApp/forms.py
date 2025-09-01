from django.forms import ModelForm

from HealthEmergencyApp.models import *


class PharmacyForm(ModelForm):
    class Meta:
        model=PharmacyModel
        fields=['PharmacyName','ContactNo','Address','Email']

class UserForm(ModelForm):
    class Meta:
        model=UserModel
        fields=['Name','Dob','Gender','MedicalHistory','Email','Address','Contact_no','Photo']

class ComplaintForm(ModelForm):
    class Meta:
        model=ComplaintModel
        fields=['Complaint','Reply']

class AmbulanceForm(ModelForm):
    class Meta:
        model=AmbulanceModel
        fields=['Driver_name','Vehicle','Vehicle_no','Availability','Contact_no'] 

class AmbulanceBookingForm(ModelForm):
    class Meta:
        model=AmbulanceBookingModel
        fields=['Date','status']

class HospitalForm(ModelForm):
    class Meta:
        model= HospitalModel
        fields=['HospitalName','Email','Contact_no','Address']

class AppointmentForm(ModelForm):
    class Meta:
        model=AppointmentModel
        fields=['Time','Token','Issue','Status']

class ReviewForm(ModelForm):
    class Meta:
        model=ReviewModel
        fields=['Review','Rating']

class DoctorForm(ModelForm):
    class Meta:
        model=DoctorModel
        fields=['DoctorName','Place','Department','Contact_no','Photo']

class BedForm(ModelForm):
    class Meta:
        model=BedModel
        fields=['RoomNo','Availability']

class BedBookingForm(ModelForm):
    class Meta:
        model=BedBookingModel
        fields=['Status','date']


class PharmacyEquipmentForm(ModelForm):
    class Meta:
        model=PharmacyEquipmentModel
        fields=['Date','MedicineName','ManufacturingDate','ExpiryDate','MedicineDescription','Photo']
        