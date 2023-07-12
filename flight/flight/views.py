from django.shortcuts import render,HttpResponse,redirect
from customers.models import *
# from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView

class bookingsApi(APIView):
    def get(self,request):
        data = booking.objects.all().values()
        # print(data)
        return Response(data)

def login(request):
    if request.method == "POST":
        user_name = request.POST.get("user")
        password_fetch = request.POST.get("password")
        all_users = user.objects.all().values()
        name_dic = {}
        for i in all_users:
            name_dic[i["name"]] = i["password"]
        print(name_dic)
        if user_name in name_dic:
            if password_fetch == name_dic[user_name]:
                return redirect("/home/")
            else:
                return HttpResponse("Password is incorrect")
        else:
            return HttpResponse("something went wrong")
    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        user_name = request.POST.get("user")
        password_fetch = request.POST.get("password")
        new_user = user(name=user_name,password=password_fetch)
        new_user.save()
        return render(request,"home.html")
    return render(request,"signup.html")

def home(request):
    dic = booking.objects.all().values()
    data=[]
    for i in dic:
        data.append(i)
    if request.method=="GET":
        var = request.GET.get("search")
        if var!=None:
            data=[]
        for i in dic:
            if i["flight_name"]==var:
                data.append(i)
    d = {"data":data}
    return render(request,"home.html",d)
    

def mybookings(request):
    if request.method == "GET":
        flight_name = request.GET.get("flight_name")
        flight_date = request.GET.get("flight_date")
        flight_arrival = request.GET.get("flight_arrival")
        flight_depart = request.GET.get("flight_depart")
        print(flight_depart)
        new_boooking = mybookings_data(flight_name=flight_name,flight_date=flight_date,flight_time_arrival=flight_arrival,flight_time_depart=flight_depart)
        new_boooking.save() 
    return redirect("/mybook/")

def mybook(request):
    dic = mybookings_data.objects.all().values()
    data=[]
    for i in dic:
        data.append(i)
    d = {
        "data":data
    }
    return render(request,"home.html",d)
