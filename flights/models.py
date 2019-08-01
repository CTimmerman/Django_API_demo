"""
User can lookup flight information based on a flight number and a date.
After searching for a flight, the following additional flight information should
be returned: airliner, departure airport, departure time, arrival airport, arrival time.
"""
from django.db import models


class Flight(models.Model):
	airliner = models.CharField(max_length=50)
	departure_airport = models.CharField(max_length=50)
	arrival_airport = models.CharField(max_length=50)
	departure_time = models.DateTimeField()
	arrival_time = models.DateTimeField()

	class Meta:
		verbose_name = "Flight"
		verbose_name_plural = "Flights"

	def __str__(self):
		return f'{self.airliner} {self.departure_time} flight {self.departure_airport} to {self.arrival_airport}'
