from django.shortcuts import render

def fetch_truck_data(request):
    return render(request,'../templates/truck.html',{})