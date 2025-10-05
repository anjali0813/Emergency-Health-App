from django.contrib import admin

from HealthEmergencyApp.models import *

# Register your models here.
admin.site.register(LoginModel)
admin.site.register(PharmacyModel)
admin.site.register(UserModel)
admin.site.register(ComplaintModel)
admin.site.register(AmbulanceModel)
admin.site.register(AmbulanceBookingModel)
admin.site.register(HospitalModel)
admin.site.register(AppointmentModel)
admin.site.register(ReviewModel)
admin.site.register(DoctorModel)
admin.site.register(PrescriptionModel)
admin.site.register(BedModel)
admin.site.register(BedBookingModel)
admin.site.register(PharmacyEquipmentModel)
admin.site.register(PharmacyBookingModel)