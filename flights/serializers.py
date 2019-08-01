from rest_framework import serializers
from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ('airliner', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time')