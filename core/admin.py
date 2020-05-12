from django.contrib import admin
from people.models import Driver

class DriverAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Driver._meta.fields]

