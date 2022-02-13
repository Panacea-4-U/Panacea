from django.shortcuts import render,redirect
from django.http import HttpResponse
from panacea_app.models import TempDb
# Create your views here.

def home(request):
    return render(request,'panacea_app/homepage.html')

def landingpage(request):
    return render(request,'panacea_app/landingpage.html')

def login_register(request):
    return render(request,'panacea_app/login_register.html')

def doctordetails(request):
    return render(request,'panacea_app/doctordetails.html')

def patientdetails(request):
    return render(request,'panacea_app/patientdetails.html')
    
def check(request):
    if(request.method=="POST"):
        temp=TempDb()
        temp.name=request.POST.get('name')
        temp.email=request.POST.get('email')
        temp.ph_no=request.POST.get('ph_no')
        temp.save()
        return redirect('/')
    return render(request,'panacea_app/check.html')
