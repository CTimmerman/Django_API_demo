from django.contrib import admin
from .models import Flight


class FlightAdmin(admin.ModelAdmin):
	list_display = ('airliner', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time')
	list_filter = list_display

admin.site.register(Flight, FlightAdmin)