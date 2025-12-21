import uuid
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
    Dob=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=40,null=True,blank=True)
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
    latitude=models.CharField(max_length=30,null=True,blank=True)
    longitude=models.CharField(max_length=30,null=True,blank=True)
    LOGIN=models.ForeignKey(LoginModel,on_delete=models.CASCADE,null=True,blank=True)


class AmbulanceModel(models.Model):
    Driver_name=models.CharField(max_length=50,null=True,blank=True)
    HOSPITAL = models.ForeignKey(HospitalModel, on_delete=models.CASCADE, null=True, blank=True)
    Vehicle_no=models.CharField(max_length=30,null=True,blank=True)
    Contact_no=models.BigIntegerField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class AmbulanceBookingModel(models.Model):
    USERID = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
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


class BookDoctor(models.Model):
    USERID = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    DOCID = models.ForeignKey(DoctorModel,on_delete=models.CASCADE,null=True,blank=True)
    Date = models.DateField(null=True,blank=True)
    Time = models.TimeField(null=True,blank=True)
    Token = models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(max_length=100,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.Token:
            self.Token = str(uuid.uuid4()).split('-')[0].upper()
        super(BookDoctor, self).save(*args, **kwargs)

class PrescriptionModel(models.Model):
    USER=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    Date=models.DateField(auto_now_add=True, null=True,blank=True)
    HOSPITAL=models.ForeignKey(HospitalModel,on_delete=models.CASCADE,null=True,blank=True)
    Prescription=models.CharField(max_length=300,null=True,blank=True)
    file = models.FileField(upload_to='prescription',null=True,blank=True)

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


class VolunteerModel(models.Model):
    LOGINID = models.ForeignKey(LoginModel, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100 , null=True , blank=True)
    Email = models.EmailField(null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Phone = models.BigIntegerField(null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    Skills = models.TextField(null=True, blank=True)
    Gender = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    Image = models.FileField(upload_to='volunteer/',null=True, blank=True)


class TaskAssignmentModel(models.Model):
    VOLUNTEERID = models.ForeignKey(VolunteerModel,on_delete=models.CASCADE,null=True,blank=True)
    TaskName = models.CharField(max_length=100, null=True, blank=True)
    TaskDescription = models.TextField(null=True, blank=True)
    TaskAddress = models.TextField(null=True, blank=True)
    TaskDate = models.DateField(null=True, blank=True)
    Status = models.CharField(max_length=100, null=True, blank=True, default="Assigned")


class FeedbackVolunteer(models.Model):
    VolunteerID = models.ForeignKey(VolunteerModel,on_delete=models.CASCADE, null=True, blank=True)
    Feedback = models.TextField(null=True, blank=True)
    Rating = models.IntegerField(null=True, blank=True)
    Created = models.DateField(auto_now_add=True)


class AlertModel(models.Model):
    Alert = models.CharField(max_length=100, null=True, blank=True)
    Latitude = models.FloatField(null=True, blank=True)
    Longitude = models.FloatField(null=True, blank=True)
    Date = models.DateTimeField(null=True, blank=True)


class BloodDonationRequestModel(models.Model):
    USERID = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    VolunteerID = models.ForeignKey(VolunteerModel,on_delete=models.CASCADE, null=True, blank=True)
    Bloodgroup=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)
