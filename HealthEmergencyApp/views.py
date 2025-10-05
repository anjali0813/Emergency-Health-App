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
        request.session['userid']=login_obj.id
        print(request.session['userid'])

        if login_obj.UserType=="admin":
            return HttpResponse('''<script>alert("admin_home");window.location=("/Homepage")</script>''')
        elif login_obj.UserType=="Hospital":
            return HttpResponse('''<script>alert("hospital_home");window.location=("/Homepage_hsptl")</script>''')
        elif login_obj.UserType=="Pharmacy":
            return HttpResponse('''<script>alert("pharmacy_home");window.location=("/Homepage_phmy")</script>''')
        else:
            return HttpResponse('''<script>alert("invalid users");window.location=("/")</script>''')
        
class Homepage(View):
    def get(self,request):
        return render(request,"Administration/homepage.html")

    
class ComplaintReply(View):
    def get(self, request):
        c=ComplaintModel.objects.all()
        return render(request, "Administration/complaint_reply.html",{'complaints':c})
    
class Reply(View):
    def get(self,request,id):
        c=ComplaintModel.objects.get(id=id)
        return render(request,"Administration/reply.html",{'replies':c})
    
    def post(self,request, id):
        c=ComplaintModel.objects.get(id=id)
        form = ReplyForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Replied successfully");window.location=("/ComplaintReply")</script>''')
   
    
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
        c=UserModel.objects.all()
        return render(request, "Administration/view_users.html",{'users':c})
    
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
        c=AmbulanceModel.objects.all()
        return render(request, "Administration/travel_facility.html",{'vehicles':c})
    
class Vehicle(View):
    def get(self,request):
        obj = HospitalModel.objects.all()
        return render(request,"Administration/vehicle.html", {'val': obj})
    
    def post(self,request):
        form=AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Successfully registered");window.location=("/")</script>''')


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
    
class ManageAppointment(View):
    def get(self, request):
        hsptl_obj=HospitalModel.objects.get(LOGIN_id=request.session['userid'])
        c=AppointmentModel.objects.filter(HOSPITAL__id=hsptl_obj.id)
        return render(request, "hospital\manage_appointments.html", {'appointments':c})
    
class ReviewRate(View):
    def get(self, request):
        c=ReviewModel.objects.all()
        return render(request, "hospital/review_rate.html",{'reviews':c})
    
class AddManageDoctors(View):
    def get(self, request):
        c=DoctorModel.objects.all()
        return render(request, "hospital/add_manage_doctors.html",{'doctors':c})
    
    def post(self, request):
        form = DoctorForm(request.POST)
        c = HospitalModel.objects.get(LOGIN__id = request.session['userid'])
        if form.is_valid():
            f=form.save(commit=False)
            f.HOSPITAL = c
        f.save()
        return HttpResponse('''<script>alert("Successfully registered");window.location=("/")</script>''')

class AddBed(View):
    def get(self, request):
        c=BedModel.objects.all()
        return render(request, "hospital/add_bed.html",{'beds':c})
    
class ViewDoctor(View):
    def get(self, request):
        c = DoctorModel.objects.all()
        return render(request, "hospital/doctors.html",{'doctors':c})
class editdoctor(View):
    def get(self,request,id):
        c=DoctorModel.objects.get(id=id)
        return render(request,"hospital/Editdoctor.html",{'doctors':c})
    def post(self,request, id):
        c=DoctorModel.objects.get(id=id)
        form=ManageDoctorForm(request.POST, instance=c)
        if form.is_valid():
            f=form.save(commit=False)
        f.save()
        return HttpResponse('''<script>alert("Successfully registered");window.location=("/ViewDoctor")</script>''')
    
class deletedoctor(View):
    def get(self,request,id):
        c=DoctorModel.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert("Successfully registered");window.location=("/ViewDoctor")</script>''')
    
class managebed(View):
    def get(self, request):
        return render(request, "hospital/managebed.html")
    def post(self,request):
        form=BedForm(request.POST)
        c = HospitalModel.objects.get(LOGIN__id = request.session['userid'])
        if form.is_valid():
            f=form.save(commit=False)
            f.HOSPITAL = c
        f.save()
        return HttpResponse('''<script>alert("Successfully registered");window.location="/AddBed"</script>''')
class deletebed(View):
    def get(self,request,id):
        c=BedModel.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert("Successfully registered");window.location=("/AddBed")</script>''')
class editbed(View):
    def get(self,request,id):
        c=BedModel.objects.get(id=id)
        return render(request,"hospital/editbed.html",{'beds':c})
    def post(self,request, id):
        c=BedModel.objects.get(id=id)
        form=BedForm(request.POST, instance=c)
        if form.is_valid():
            f=form.save(commit=False)
        f.save()
        return HttpResponse('''<script>alert("Successfully registered");window.location=("/AddBed")</script>''') 
    
class AddManagePrescription(View):
    def get(self,request):
        c=PrescriptionModel.objects.all()
        return render(request,"Hospital/add_manage_prescription.html")
    

class AddPrescription(View):
    def get(self,request):
        return render(request,"Hospital\prescription.html")   

    #////////////////////////////////// PHARMACY ////////////////////////////
class addequipment(View):
    def get(self,request):
        return render(request,"pharmacy/addequipment.html")
    def post(self,request):
        form=PharmacyEquipmentForm(request.POST, request.FILES)
        c=PharmacyModel.objects.get(LOGIN__id=request.session['userid'])
        if form.is_valid():
            f=form.save(commit=False)
            f.PHARMACY = c
            f.save()
            return HttpResponse('''<script>alert("Successfully registered");window.location=("/PharmacyEquipments")</script>''') 
    


class PharmacyEquipments(View):
    def get(self, request):
        c=PharmacyEquipmentModel.objects.all()
        print('--------------------------------------------->',c)
        return render(request, "pharmacy/pharmacy_equipments.html",{'equipments':c})
    
    
    
class ManageBooking(View):
    def get(self, request):
        c=PharmacyBookingModel.objects.all()
        return render(request, "pharmacy/manage_booking.html",{'pharmacybooking':c})
 
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


class AcceptBooking(View):
    def get(self,request,id):
        c=PharmacyBookingModel.objects.get(id=id)
        c.Status='Booked'
        c.save()
        return HttpResponse('''<script>alert("Verified successfully");window.location=("/ManageBooking")</script>''')
    
class RejectBooking(View):
    def get(self,request,id):
        c=PharmacyBookingModel.objects.get(id=id)
        c.Status='Rejected'
        c.save()
        return HttpResponse('''<script>alert("Not verified");window.location=("/ManageBooking")</script>''')
