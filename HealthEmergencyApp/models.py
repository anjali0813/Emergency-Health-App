from django.db import models

# Create your models here.
class LoginModel(models.Model):
    Username=models.CharField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=40,null=True,blank=True)
    UserType=models.CharField(max_length=30,null=True,blank=True)


class PharmacyModel(models.Model):
    PharmacyName=models.CharField(max_length=40,null=True,blank=True)
    ContactNo=models.BigIntegerField(null=True,blank=True)
    Address=models.CharField(max_length=40,null=True,blank=True)
    Email=models.CharField(max_length=40,null=True,blank=True)
    LOGIN=models.ForeignKey(LoginModel,on_delete=models.CASCADE,null=True,blank=True)


class UserModel(models.Model):
    LOGIN=models.ForeignKey(LoginModel,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=30,null=True,blank=True)
    Dob=models.DateField(null=True,blank=True)
    Gender=models.CharField(max_length=40,null=True,blank=True)
    MedicalHistory=models.CharField(max_length=40,null=True,blank=True)
    Email=models.CharField(max_length=40,null=True,blank=True)
    Address=models.CharField(max_length=40,null=True,blank=True)
    Contact_no=models.BigIntegerField(null=True,blank=True)
    Photo = models.FileField(upload_to='userprofile/',null=True, blank=True)


class ComplaintModel(models.Model):
    Date=models.DateField(auto_now_add=True,null=True,blank=True)
    USER=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    Complaint=models.CharField(max_length=500)
    Reply=models.CharField(max_length=50, null=True, blank=True)



class HospitalModel(models.Model):
    HospitalName=models.CharField(max_length=30,null=True,blank=True)
    Email=models.CharField(max_length=30,null=True,blank=True)
    Contact_no=models.BigIntegerField(null=True,blank=True)
    Address=models.CharField(max_length=30,null=True,blank=True)
    LOGIN=models.ForeignKey(LoginModel,on_delete=models.CASCADE,null=True,blank=True)


class AmbulanceModel(models.Model):
    Driver_name=models.CharField(max_length=50,null=True,blank=True)
    HOSPITAL = models.ForeignKey(HospitalModel, on_delete=models.CASCADE, null=True, blank=True)
    Vehicle_no=models.CharField(max_length=30,null=True,blank=True)
    Contact_no=models.BigIntegerField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class AmbulanceBookingModel(models.Model):
    AMBULANCE = models.ForeignKey(AmbulanceModel, on_delete=models.CASCADE, null=True, blank=True)
    Date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)



class AppointmentModel(models.Model):
    USER=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    HOSPITAL=models.ForeignKey(HospitalModel,on_delete=models.CASCADE,null=True,blank=True)
    Date=models.DateField(auto_now_add=True, null=True,blank=True)
    Time=models.IntegerField(null=True,blank=True)
    Token=models.IntegerField(null=True,blank=True)
    Issue=models.CharField(max_length=50,null=True,blank=True)
    Status=models.CharField(max_length=30,null=True,blank=True)


class ReviewModel(models.Model):
    USER=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    HOSPITAL=models.ForeignKey(HospitalModel,on_delete=models.CASCADE,null=True,blank=True)
    Date=models.DateField(auto_now_add=True, null=True,blank=True)
    Review=models.CharField(max_length=300,null=True,blank=True)
    Rating=models.FloatField(null=True,blank=True)


class DoctorModel(models.Model):
    HOSPITAL=models.ForeignKey(HospitalModel,on_delete=models.CASCADE,null=True,blank=True)
    DoctorName=models.CharField(max_length=30,null=True,blank=True)
    Place=models.CharField(max_length=40,null=True,blank=True)
    Department=models.CharField(max_length=30,null=True,blank=True)
    contact_no=models.IntegerField(null=True,blank=True)
    Photo = models.FileField(null=True, blank=True)


class PrescriptionModel(models.Model):
    USER=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    Date=models.DateField(auto_now_add=True, null=True,blank=True)
    HOSPITAL=models.ForeignKey(HospitalModel,on_delete=models.CASCADE,null=True,blank=True)
    Prescription=models.FileField(null=True,blank=True)
    Description=models.CharField(max_length=500,null=True,blank=True)
    Status=models.CharField(max_length=30,null=True,blank=True)

class BedModel(models.Model):
    count=models.IntegerField(null=True,blank=True)
    ward=models.CharField(max_length=30,null=True,blank=True)
    HOSPITAL=models.ForeignKey(HospitalModel,on_delete=models.CASCADE,null=True,blank=True)


class BedBookingModel(models.Model):
    USER=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    BED=models.ForeignKey(BedModel,on_delete=models.CASCADE,null=True,blank=True)
    Status=models.CharField(max_length=30,null=True,blank=True)
    date = models.DateField(null=True, blank=True)


class PharmacyEquipmentModel(models.Model):
    PHARMACY=models.ForeignKey(PharmacyModel,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateField(null=True,blank=True, auto_now_add=True)
    MedicineName=models.CharField(max_length=30,null=True,blank=True)
    ManufacturingDate=models.DateField(null=True,blank=True)
    ExpiryDate=models.DateField(null=True,blank=True)
    MedicineDescription=models.CharField(max_length=50,null=True,blank=True)
    MEDICINE=models.IntegerField(null=True,blank=True)
    Photo = models.FileField(null=True, blank=True, upload_to='equipment')

class PharmacyBookingModel(models.Model):
    PRESCRIPTION=models.ForeignKey(PrescriptionModel,on_delete=models.CASCADE,null=True,blank=True)
    Date=models.DateField(null=True,blank=True)
    Status=models.CharField(max_length=30,null=True,blank=True)
