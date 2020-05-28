from django.db import models
from multiselectfield import MultiSelectField
from rest_framework import serializers
class Driver(models.Model):
    name = models.CharField(max_length=200)
    license_choices = (('AM', 'AM (Very lightweight motorbike)'),
                       ('A1', 'A1 (Lightweight motorbike)'),
                       ('A2', 'A2 (Middleweight motorbike)'),
                       ('A', 'A (All motorbikes)'),
                       ('B1', 'B1 (Light cars)'),
                       ('B', 'B (Cars)'),
                       ('C1', 'C1 (Lightweight trucks)'),
                       ('C', 'C (Trucks)'),
                       ('D1', 'D1 (Lightweight touring cars'),
                       ('D', 'D (Touring Cars)'),
                       ('BE', 'BE (Trailers for cars)'),
                       ('C1E', 'C1E (Trailers for lightweight trucks)'),
                       ('CE', 'CE (Trailers for trucks)'),
                       ('D1E', 'D1E (Trailers for lightweight touring cars)'),
                       ('DE', 'DE (Trailers for touring cars)'),
                       ('T', 'T (Agricultural vehicles)'),
                       ('OC', 'Non-European car'),
                       ('OM', 'Non-European motorbike'),
                       ('OTR', 'Non-European truck'),
                       ('OTC', 'Non-European touring car'),
                       ('OA', 'Non-European touring agricultural'))

    license_type = MultiSelectField(choices=license_choices,max_length=70,verbose_name=('License Type(s)'))
    def __str__(self):
        return self.name