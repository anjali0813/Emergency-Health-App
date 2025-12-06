from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from HealthEmergencyApp.models import *
class Regserializer(ModelSerializer):
    class Meta:
        model=UserModel
        fields='__all__'

class Logserializer(ModelSerializer):
    class Meta:
        model=LoginModel
        fields='__all__'

####################################################################################################

class Hospitalserializer(ModelSerializer):
    class Meta:
        model=HospitalModel
        fields='__all__'

class Doctorserializer(ModelSerializer):
    class Meta:
        model=DoctorModel
        fields='__all__'

class DoctorBookserializer(ModelSerializer):
    class Meta:
        model=BookDoctor
        fields='__all__'

class Reviewserializer(ModelSerializer):
    class Meta:
        model=ReviewModel
        fields='__all__'

class BookingHistorydoctor(ModelSerializer):
    Doctor_name = serializers.CharField(source='DOCID.DoctorName')
    Hosp_name = serializers.CharField(source='DOCID.HOSPITAL.HospitalName')
    Hosp_id = serializers.CharField(source='DOCID.HOSPITAL.id')
    class Meta:
        model = BookDoctor
        fields='__all__'

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintModel
        fields='__all__'

class AmbulanceSerializer(serializers.ModelSerializer):
    hospital_name=serializers.CharField(source='HOSPITAL.Hospital_name',read_only=True)
    class Meta:
        model=AmbulanceModel
        fields=['id','Driver_name','Vehicle_no','Contact_no','hospital_name','HOSPITAL']


class AmbulanceBookingSerializer(serializers.ModelSerializer):
    ambulance_details=AmbulanceSerializer(source='AMBULANCE',read_only=True)
    class Meta:
        model=AmbulanceBookingModel
        fields=['id','AMBULANCE','Date','status','ambulance_details']


class AmbulanceBookingHistorySerializer(serializers.ModelSerializer):
    hospital_name=serializers.CharField(source='AMBULANCE.HOSPITAL.Hospital_name',read_only=True)
    driver_name = serializers.CharField(source='AMBULANCE.Driver_name', read_only=True)
    vehicle_no=serializers.CharField(source='AMBULANCE.Vehicle_no',read_only=True)
    class Meta:
        model=AmbulanceBookingModel
        fields=['id','hospital_name','driver_name','vehicle_no','Date','status']


class BedBookingSerializer(ModelSerializer):
    class Meta:
        model= BedBookingModel
        fields=['BED','date']

class BedSerializer(ModelSerializer):
    bed_id=serializers.IntegerField(source='id')
    class Meta:
        model=BedModel
        fields=['count','ward','bed_id']

class BedBookingHistorySerializer(serializers.ModelSerializer):
    hospital_name=serializers.CharField(source='BED.HOSPITAL.Hospitalname',read_only=True)
    ward=serializers.CharField(source='BED.ward',read_only=True)
    bed_id=serializers.IntegerField(source='BED.id',read_only=True)
    user_name=serializers.CharField(source='USER.Name',read_only=True)
    
    class Meta:
        model=BedBookingModel
        fields=['id','bed_id','ward','hosptal_name','status','date','user_name']