from rest_framework.serializers import ModelSerializer

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