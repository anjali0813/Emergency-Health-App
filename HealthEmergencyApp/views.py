from datetime import datetime, timedelta, time as dtime
import uuid
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from HealthEmergencyApp.forms import *
from HealthEmergencyApp.models import *
from HealthEmergencyApp.serializers import *

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
        return render(request,"Hospital/add_manage_prescription.html",{'prescriptions':c})
    

class AddPrescription(View):
    def get(self,request):
        c = UserModel.objects.all()
        return render(request,"Hospital\prescription.html",{'user':c})   
    def post(self,request):
        c=HospitalModel.objects.get(LOGIN__id=request.session['userid'])
        d=AddManagePrescriptionForm(request.POST,request.FILES)
        if d.is_valid():
            reg=d.save(commit=False)
            reg.HOSPITAL = c
            reg.save()
            return HttpResponse('''<script>alert("Successfully added");window.location=("/add_manage_prescription")</script>''')

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
    
##############################################################################################################################

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class UserReg_api(APIView):
    def post(self, request):
        print("#########################3", request.data)

        user_serial = Regserializer(data=request.data)
        login_serial = Logserializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(UserType='USER')

            # Assign the login profile to the UserTable and save the UserTable
            user_serial.save(LOGIN=login_profile)

            # Return the serialized user data in the response
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        
        return Response({
            'login_error' : login_serial.errors if not login_valid else None,
            'user_error' : user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LoginPage_api(APIView):
    def post(self, request):
        print(request.data)

        username = request.data.get("Username")
        password = request.data.get("Password")
        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")

        if not username or not password:
            return Response(
                {"message": "Failed"},
                status=status.HTTP_400_BAD_REQUEST
            )

        t_user = LoginModel.objects.filter(
            Username=username,
            Password=password
        ).first()

        if not t_user:
            return Response(
                {"message": "Failed"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # 🔵 VOLUNTEER
        if t_user.UserType == "Volunteer":
            volunteer = VolunteerModel.objects.get(LOGINID_id=t_user.id)
            volunteer.latitude = latitude
            volunteer.longitude = longitude
            volunteer.save()

        # 🟢 USER
        elif t_user.UserType == "USER":
            user = UserModel.objects.get(LOGIN_id=t_user.id)
            user.latitude = latitude
            user.longitude = longitude
            user.save()

        # ✅ RETURN RESPONSE FOR ALL CASES
        return Response(
            {
                "message": "success",
                "login_id": t_user.id,
                "UserType": t_user.UserType
            },
            status=status.HTTP_200_OK
        )



class ViewHospitalAPI(APIView):
    def get(self,request):
        c=HospitalModel.objects.all()
        serializer=Hospitalserializer(c, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ViewDoctorAPI(APIView):
    def get(self,request,id):
        d=DoctorModel.objects.filter(HOSPITAL__id=id)
        serializer=Doctorserializer(d,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookDoctorApi(APIView):
    def post(self, request, id):
        print('========================', request.data)

        # Get user
        try:
            user = UserModel.objects.get(LOGIN_id=id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        # Get doctor
        doctor_id = request.data.get("DOCID")
        try:
            doctor = DoctorModel.objects.get(id=doctor_id)
        except DoctorModel.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=404)

        # Working hours
        start_hour = 9
        end_hour = 17
        slot_duration_minutes = 30

        # Existing bookings
        bookings = BookDoctor.objects.filter(DOCID=doctor).order_by('Date', 'Time')

        today = datetime.now().date()
        next_slot = None

        # Find next available slot
        for day_offset in range(0, 30):
            check_date = today + timedelta(days=day_offset)
            current_time = dtime(start_hour, 0)

            while current_time < dtime(end_hour, 0):
                if not bookings.filter(Date=check_date, Time=current_time).exists():
                    next_slot = (check_date, current_time)
                    print("=========== Found slot:", next_slot)
                    break

                # Move time slot ahead
                full_datetime = datetime.combine(check_date, current_time) + timedelta(minutes=slot_duration_minutes)
                current_time = full_datetime.time()

            if next_slot:
                break

        # If no slot available
        if not next_slot:
            return Response({"error": "No available slots in the next 30 days"}, status=400)

        # Create booking
        token = str(uuid.uuid4()).split('-')[0].upper()

        booking = BookDoctor.objects.create(
            USERID=user,
            DOCID=doctor,
            Date=next_slot[0],
            Time=next_slot[1],
            Token=token,
            Status="pending"
        )

        serializer = DoctorBookserializer(booking)
        return Response(serializer.data, status=201)



class BookingHis(APIView):
    def get(self,request,id):
        c = BookDoctor.objects.filter(USERID__LOGIN_id = id)
        serializers = BookingHistorydoctor(c, many=True)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    

class AddReview(APIView):
    def post(self,request,id):
        c = UserModel.objects.get(LOGIN_id = id)
        d = Reviewserializer(data = request.data)
        if d.is_valid():
            d.save(USER = c)
            return Response(d.data,status=status.HTTP_200_OK)
        return Response(d.error,status=status.HTTP_400_BAD_REQUEST)


class AddComplaintAPI(APIView):
    def get(self,request,id):
        c = ComplaintModel.objects.filter(USER__LOGIN_id = id)
        serializer = ComplaintSerializer(c,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,id):
        try:
            c=UserModel.objects.get(LOGIN_id=id)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"},status=status.HTTP_404_NOT_FOUND)
        
        d=ComplaintSerializer(data=request.data)
        if d.is_valid():
            d.save(USER=c)
            print('===============================================',d.data)
            return Response(d.data,status=status.HTTP_200_OK)
        else:
            print('Validation error:' ,d.error)
            return Response(d.errors, status=status.HTTP_400_BAD_REQUEST)
        

class AmbulancebookingAPI(APIView):
    def post(self,request,lid,ambulance_id):

        # step 1: get user by login ID
        user = UserModel.objects.get(LOGIN__id=lid)
        print('-------------------->', user)
        if not user:
            return Response({'error':'User not found for this login ID'}, status=status.HTTP_404_NOT_FOUND)
        
        #step 2: get ambulance by ID
        try:
            ambulance=AmbulanceModel.objects.get(id=ambulance_id)
            print('====================================>', ambulance)
        except AmbulanceModel.DoesNotExist:
            return Response({'error':'Ambulance not found'},status=status.HTTP_404_NOT_FOUND)
        
        #step 3: validate date
        date = request.data.get('Date')
        if not date:
            return Response({'error': 'Date is required'},status=status.HTTP_400_BAD_REQUEST)
        
        #step4 : create booking and assign user
        booking = AmbulanceBookingModel.objects.create(
            AMBULANCE = ambulance,
            Date = date,
            status = 'pending',
            USERID = user    #<--assigned here
        )

        #step 5: serialize and return response
        serializer=AmbulanceBookingSerializer(booking)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class AmbulanceBookingHistoryAPI(APIView):
    def get(self,request,lid):
        try:
            user=UserModel.objects.get(LOGIN_id=lid)
        except UserModel.DoesNotExist:
            return Response({"error":"User not found"},status=404)
            
        bookings=AmbulanceBookingModel.objects.filter(USERID=user).order_by('-Date')
        serializer= AmbulanceBookingHistorySerializer(bookings,many=True)
        return Response(serializer.data,status=200)
        
class AmbulanceByHospitalAPI(APIView):
    def get(self,request,hospital_id):
        ambulances=AmbulanceModel.objects.filter(HOSPITAL_id=hospital_id)
        serializer=AmbulanceSerializer(ambulances,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
            

class BedBookingAPI(APIView):
    def post(self,request,id):
        print('===================================',request.data)
        try:
            #Get User
            user=UserModel.objects.get(LOGIN_id=id)
            print('--------------------------------', user)
        except UserModel.DoesNotExist:
            return Response({"error":"User not found"},status=status.HTTP_404_NOT_FOUND)

        serializer=BedBookingSerializer(data=request.data)
        if serializer.is_valid():
            bed_id=request.data.get("BED")

            #check if bed exists
            try:
                bed=BedModel.objects.get(id=bed_id)
            except BedModel.DoesNotExist:
                return Response({"error":"Bed not found"},status=status.HTTP_404_NOT_FOUND)
            
            #check if bed count is available
            if bed.count is None or bed.count<=0:
                return Response({"error":"No beds available in this ward"},status=status.HTTP_400_BAD_REQUEST)
            
            #save booikng with default status = "pending"
            booking=serializer.save(USER=user, Status="pending")

            #reduce bed count
            bed.count-=1
            bed.save()

            #Return response
            return Response({
                "message":"Bed booked successfully",
                "booking":BedBookingSerializer(booking).data,
                "remaining_beds":bed.count
            },status=status.HTTP_200_OK)
        
        #handle serializer validation errors
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class BedBookingHistoryAPI(APIView):
    def get(self,request,id):
        try:
            user=UserModel.objects.get(LOGIN_id=id)
        except UserModel.DoesNotExist:
            return Response({"error":"user not found"},status=status.HTTP_404_NOT_FOUND) 

        bookings= BedBookingModel.objects.filter(USER=user).order_by('-date')
        serializer=BedBookingHistorySerializer(bookings,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

        

class ViewBedAPI(APIView):
    def get(self,request,id):
        print('=====================================',request.data)
        c=BedModel.objects.filter(HOSPITAL_id=id)
        serializer=BedSerializer(c,many=True)
        print('-----------------------------------------------',serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class VolunteerRegAPI(APIView):
    def post(self,request):
        print("#####################################",request.data)

        user_serial = VolunteerSerializer(data=request.data)
        login_serial = Logserializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(UserType = "Volunteer")

            # Assign the login profile to the usertable and save the usertable 
            user_serial.save(LOGINID = login_profile)

            # return te  serialized user data in the response
            return Response(user_serial.data,status=status.HTTP_201_CREATED)
        
        return Response({
            'login_error':login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status==status.HTTP_400_BAD_REQUEST)
    
class VolunteerProfileAPI(APIView):
    def get(self,request,lid):
        print(lid)
        c=VolunteerModel.objects.get(LOGINID_id = lid)
        d=VolunteerSerializer(c)
        return Response(d.data,status=status.HTTP_200_OK)
    def put(self,request,lid):
        user = VolunteerModel.objects.get(LOGINID_id=lid)
        serializer = VolunteerSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    

class ViewTaskAssignmentAPI(APIView):

    def get(self, request, lid):
        tasks = TaskAssignmentModel.objects.filter(
            VOLUNTEERID__LOGINID__id=lid
        )
        serializer = TaskAssignmentSerializer(tasks, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, lid):
        try:
            task = TaskAssignmentModel.objects.get(id=lid)
        except TaskAssignmentModel.DoesNotExist:
            return Response({"Error": "Task not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = TaskAssignmentSerializer(
            task, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VolunteerFeedbackAPI(APIView):
    def post(self,request,lid):
        print(request.data)
        try:
            c = VolunteerModel.objects.get(LOGINID_id=lid)
        except VolunteerModel.DoesNotExist:
            return Response({"Error" : "Volunteer not found"},status=status.HTTP_404_NOT_FOUND)
        
        d =VolunteerFeedbackSerializer(data=request.data)
        if d.is_valid():
            d.save(VolunteerID=c)
            return Response(d.data,status=status.HTTP_200_OK)
        return Response(d.errors,status=status.HTTP_400_BAD_REQUEST)
    

class PublicAlertAPI(APIView):
    def get(self,request):
        c = AlertModel.objects.all()
        serializer = PublicAlertSerializer(c,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class BloodDonationRequestAPI(APIView):
    def post(self,request,id):
        c = UserModel.objects.get(LOGIN__id=id)
        d = BloodDonationRequestSerializer(data=request.data)
        if d.is_valid():
            d.save(USERID=c, status="pending")
            return Response(d.data,status=status.HTTP_200_OK)
        

class ViewAlertAPI(APIView):
    def get(self,request):
        c = AlertModel.objects.all()
        ser = PublicAlertSerializer(c, many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    

class ViewBloodReq(APIView):
    def get(self, request):
        c = BloodDonationRequestModel.objects.filter(status="pending")
        d = RequestSerializer(c, many=True)
        return Response(d.data, status=status.HTTP_200_OK)
    

class ReqHistory(APIView):
    def get(self, request, id):
        c= BloodDonationRequestModel.objects.filter(VolunteerID__LOGINID__id = id)
        ser = RequestSerializer(c, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

class AcceptReq(APIView):
    def post(self, request, id):
        try:
            blood_request = BloodDonationRequestModel.objects.get(id=id)

            volunteer_id = request.data.get('VolunteerID')

            if not volunteer_id:
                return Response(
                    {"message": "VolunteerID required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            volunteer = VolunteerModel.objects.get(LOGINID__id=volunteer_id)

            blood_request.VolunteerID = volunteer
            blood_request.status = "Accepted"
            blood_request.save()

            return Response(
                {
                    "message": "Request accepted successfully",
                    "request_id": blood_request.id,
                    "VolunteerID": volunteer.id,
                    "status": blood_request.status
                },
                status=status.HTTP_200_OK
            )

        except BloodDonationRequestModel.DoesNotExist:
            return Response(
                {"message": "Blood request not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        except VolunteerModel.DoesNotExist:
            return Response(
                {"message": "Volunteer not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class AddAlertApi(APIView):
    def post(self, request):
        c = PublicAlertSerializer(data=request.data)
        if c.is_valid():
            c.save()
            return Response(c.data, status=status.HTTP_200_OK)
    def get(self, request):
        c = AlertModel.objects.all().order_by('-Date').first()
        d = PublicAlertSerializer(c)
        return Response(d.data, status=status.HTTP_200_OK)


from openai import OpenAI
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatBotModel, UserModel
import re
# =====================================
# OPENROUTER CLIENT (FREE MODEL)
# =====================================

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# =====================================
# FIRST AID CHATBOT API
# =====================================

class ChatBotAPI(APIView):

    # ---------------- POST : SEND SYMPTOMS ----------------
    def post(self, request, user_id):
        try:
            symptoms = request.data.get("message", "").strip()

            if not symptoms:
                return Response(
                    {"error": "Symptoms are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # LOGIN ID from URL
            user = UserModel.objects.get(LOGIN__id=user_id)

            # FETCH LAST 6 CHATS
            history = ChatBotModel.objects.filter(
                user=user
            ).order_by("timestamp")[:6]

            # SYSTEM PROMPT: short advice + department
            messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are a medical first-aid assistant. "
                            "Give ONLY short first-aid instructions in 2-3 sentences. "
                            "Do NOT diagnose diseases. "
                            "Do NOT prescribe medicines. "
                            "ALWAYS include the most relevant medical department for consultation in the exact format: "
                            "'Department: <department name>' at the end. "
                            "End your advice with: 'Consult a doctor if symptoms worsen.'"
                        )
                    }
                ]

            # ADD CHAT HISTORY
            for chat in history:
                messages.append({"role": "user", "content": chat.Message})
                messages.append({"role": "assistant", "content": chat.botResponse})

            # CURRENT USER MESSAGE
            messages.append({
                "role": "user",
                "content": f"My symptoms are: {symptoms}"
            })

            # OPENROUTER API CALL
            response = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free",
                messages=messages,
                temperature=0.3
            )

            if not response.choices:
                return Response(
                    {"error": "AI did not respond"},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )

            bot_reply = response.choices[0].message.content.strip()
            bot_reply = re.sub(r"<.*?>|\[.*?\]", "", bot_reply).strip()

            # Extract department using exact "Department: ..." format
            department_match = re.search(r"Department:\s*(.+)", bot_reply)
            if department_match:
                department = department_match.group(1).strip()
            else:
                department = "General Physician"  # fallback


            # SAVE CHAT HISTORY
            ChatBotModel.objects.create(
                user=user,
                Message=symptoms,
                botResponse=bot_reply
            )

            return Response(
                {
                    "login_id": user.LOGIN.id,
                    "symptoms": symptoms,
                    "first_aid_advice": bot_reply,
                    "department": department
                },
                status=status.HTTP_200_OK
            )

        except UserModel.DoesNotExist:
            return Response(
                {"error": "User not found for this login ID"},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            print("ERROR:", e)
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    # ---------------- GET : CHAT HISTORY ----------------
    def get(self, request, user_id):
        try:
            user = UserModel.objects.get(LOGIN__id=user_id)

            chats = ChatBotModel.objects.filter(
                user=user
            ).order_by("-timestamp")

            history = [
                {
                    "message": chat.Message,
                    "response": chat.botResponse,
                    "time": chat.timestamp
                }
                for chat in chats
            ]

            return Response(
                {"history": history},
                status=status.HTTP_200_OK
            )

        except UserModel.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

