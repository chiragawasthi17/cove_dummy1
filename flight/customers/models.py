from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200) 

class booking(models.Model):
    flight_name = models.CharField(max_length=200)
    flight_date = models.DateField()
    flight_time_depart = models.TimeField()
    flight_time_arrival = models.TimeField()

class mybookings_data(models.Model):
    flight_name = models.CharField(max_length=200)
    flight_date = models.CharField(max_length=200)
    flight_time_depart =  models.CharField(max_length=200)
    flight_time_arrival =  models.CharField(max_length=200)
