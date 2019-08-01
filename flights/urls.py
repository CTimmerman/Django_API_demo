
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('', views.FlightView, basename='Flight')

urlpatterns = [
	path('api', include(router.urls)),
	path('', views.flight_list),
	path('<int:id>/', views.flight_detail, name='detail'),
]
