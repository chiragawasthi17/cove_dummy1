from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# import rest_framework.response import Response
# from rest_framework.views import APIview
# from rest_framework.response import Response
from .models import *

class bookingsApi(APIView):
    def get(self,request):
        data = booking.objects.all().values()
        print(data)
        return Response(data)
        

# Create your views here.
