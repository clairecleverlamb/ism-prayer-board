from django.contrib import admin

# Register your models here.
from .models import PrayerRequest

admin.site.register(PrayerRequest)