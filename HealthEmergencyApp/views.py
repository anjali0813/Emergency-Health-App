from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from HealthEmergencyApp.forms import *
from HealthEmergencyApp.models import *

# Create your views here.
# /////////////////////////////////////////// ADMIN /////////////////////////////////////////////
class LoginPage(View):
    def get(self, request):
        return render(request, "Administration/login.html")
    def post(self,request):
        Username1=request.POST['Username']
        Password1=request.POST['Password']

        login_obj=LoginModel.objects.get(Username=Username1,Password=Password1)

        if login_obj.UserType=="admin":
            return HttpResponse('''<script>alert("admin_home");window.location=("/Homepage")</script>''')
        elif login_obj.UserType=="hospital":
            return HttpResponse('''<script>alert("hospital_home");window.location=("/Homepage_hsptl")</script>''')
        elif login_obj.UserType=="pharmacy":
            return HttpResponse('''<script>alert("pharmacy_home");window.location=("/Homepage_phmy")</script>''')
        else:
            return HttpResponse('''<script>alert("invalid users");window.location=("/")</script>''')
        
class Homepage(View):
    def get(self,request):
        return render(request,"Administration/homepage.html")

    
class ComplaintReply(View):
    def get(self, request):
        return render(request, "Administration/complaint_reply.html")
    
class VerifyHospital(View):
    def get(self, request):
        c=HospitalModel.objects.all()
        return render(request, "Administration/verify_hospital.html",{'hospitals':c})
    
class AcceptHospital(View):
    def get(self,request,id):
        c=HospitalModel.objects.get(id=id)
        c.LOGIN.UserType='Hospital'
        c.LOGIN.save()
        return HttpResponse('''<script>alert("Verified successfully");window.location=("/VerifyHospital")</script>''')
    
class RejectHospital(View):
    def get(self,request,id):
        c=HospitalModel.objects.get(id=id)
        c.LOGIN.UserType='Rejected'
        c.LOGIN.save()
        return HttpResponse('''<script>alert("Not verified");window.location=("/VerifyHospital")</script>''')


    
class ViewUsers(View):
    def get(self, request):
        return render(request, "Administration/view_users.html")
    
class VerifyPharmacy(View):
    def get(self, request):
        c=PharmacyModel.objects.all()
        return render(request, "Administration/verify_pharmacy.html",{'pharmacies':c})
    
class AcceptPharmacy(View):
    def get(self,request,id):
        c=PharmacyModel.objects.get(id=id)
        c.LOGIN.UserType='Pharmacy'
        c.LOGIN.save()
        return HttpResponse('''<script>alert("Verified successfully");window.location=("/VerifyPharmacy")</script>''')
    
class RejectPharmacy(View):
    def get(self,request,id):
        c=PharmacyModel.objects.get(id=id)
        c.LOGIN.UserType='Rejected'
        c.LOGIN.save()
        return HttpResponse('''<script>alert("Not verified");window.location=("/VerifyPharmacy")</script>''')

class TravelFacility(View):
    def get(self, request):
        return render(request, "Administration/travel_facility.html")


    # /////////////////////////////////////////// HOSPITAL ///////////////////////////////////////////
    
class Register_hsptl(View):
    def get(self, request):
        form = HospitalForm()
        return render(request, "hospital/register_hsptl.html", {"form": form})

    def post(self, request):
        form = HospitalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.LOGIN = LoginModel.objects.create(
                Username=request.POST['Username'],
                Password=request.POST['Password'],
                UserType="pending"
            )
            f.save()
            return HttpResponse('''<script>alert("Successfully registered");window.location=("/")</script>''')

    
class Homepage_hsptl(View):
    def get(self,request):
        return render(request,"hospital/homepage_hsptl.html")
    
class BookAppointment(View):
    def get(self, request):
        return render(request, "hospital/book_appointments.html")
    
class ReviewRate(View):
    def get(self, request):
        return render(request, "hospital/review_rate.html")
    
class AddManageDoctors(View):
    def get(self, request):
        return render(request, "hospital/add_manage_doctors.html")
 

class AddBed(View):
    def get(self, request):
        return render(request, "hospital/bed_booking.html")
    
    #////////////////////////////////// PHARMACY ////////////////////////////
 
class PharmacyEquipments(View):
    def get(self, request):
        return render(request, "pharmacy/pharmacy_equipments.html")
    
class ManageBooking(View):
    def get(self, request):
        return render(request, "pharmacy/manage_booking.html")
 
class Homepage_phmy(View):
    def get(self,request):
        return render(request,"pharmacy/homepage_phmy.html")
    
class Register_phmy(View):
    def get(self, request):
        return render(request, "pharmacy/register_phmy.html")
    
    def post(self, request):
        form = PharmacyForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.LOGIN = LoginModel.objects.create(
                Username=request.POST['Username'],
                Password=request.POST['Password'],
                UserType="pending"
            )
            f.save()
            return HttpResponse('''<script>alert("Successfully registered");window.location=("/")</script>''')
