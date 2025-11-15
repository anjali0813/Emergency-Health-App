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
