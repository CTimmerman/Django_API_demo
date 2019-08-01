from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer


class FlightView(viewsets.ModelViewSet):
	serializer_class = FlightSerializer
	def get_queryset(self):
		queryset = Flight.objects.all()
		flight_number = self.request.query_params.get('flight_number', None)
		if flight_number is not None:
			queryset = queryset.filter(id=flight_number)
		departure_time = self.request.query_params.get('departure_time', None)
		if departure_time is not None:
			queryset = queryset.filter(departure_time=departure_time)
		arrival_time = self.request.query_params.get('arrival_time', None)
		if arrival_time is not None:
			queryset = queryset.filter(arrival_time=arrival_time)
		return queryset

def flight_list(request):
	flights = Flight.objects.all()
	return render(request, 'list.html', {'flights': flights})

def flight_detail(request, id):
	flight = get_object_or_404(Flight, id=id)
	return render(request, 'detail.html', {'flight': flight})