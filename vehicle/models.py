from django.db import models
from django.utils.translation import gettext_lazy as _

class Vehicle(models.Model):
    # type_of_vehicle, brand, model, license_plate, identification, fuel_type
    class TypeOfVehicle(models.TextChoices):
        CAR = 'CAR', _('Car')
        MOTORBIKE = 'MOT', _('Motorbike')
        TRUCK = 'TRU', _('Truck')
        ATV = 'ATV', _('ATV/Quad')
        TRAILER = 'TRA', _('Trailer')
        OTHER = 'OTH', _('Other')

    type_of_vehicle = models.CharField(max_length=3,choices=TypeOfVehicle.choices,default=TypeOfVehicle.CAR)
    brand = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    license_plate = models.CharField(max_length=10,default="XX-XX-XX",verbose_name=('License Plate '),blank=True)
    identification = models.CharField(max_length=20,default="",verbose_name=('Identification/Serial number (VIN) '),blank=True)
    year = models.DateField('Date of first registration (Production Year)',help_text="Enter the date of first registration of your vehicle or January first of the year of production if first registration date is unknown")
    date_of_purchase =models.DateField('Date of purchase')
    def __str__(self):
        return self.brand + ' ' + self.type