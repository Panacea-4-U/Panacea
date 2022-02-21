from django.shortcuts import render,redirect
from django.http import HttpResponse
from panacea_app.models import Patient, TempDb
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def home(request):
    return render(request,'panacea_app/homepage.html')

def landingpage(request):
    return render(request,'panacea_app/landingpage.html')

def login_register(request):
    if (request.method == "POST"):
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpass = request.POST.get("confpass")
        category = request.POST.get("category")
        if(password == confpass ):
            if (category == "Patient"):
                patient = Patient()
                patient.name = name
                patient.email = email
                patient.password = password
                patient.save()
                return redirect('pat-home',pk=email)
    return render(request,'panacea_app/login_register.html')

def doctordetails(request):
    return render(request,'panacea_app/doctordetails.html')

def patientdetails(request):
    return render(request,'panacea_app/patientdetails.html')

def contact_us(request):
    return render(request, 'panacea_app/contact_us.html')
		
def about_us(request):
    return render(request, 'panacea_app/about_us.html')
    
def check(request):
    if(request.method=="POST"):
        temp=TempDb()
        temp.name=request.POST.get('name')
        temp.email=request.POST.get('email')
        temp.ph_no=request.POST.get('ph_no')
        temp.save()
        return redirect('/')
    return render(request,'panacea_app/check.html')

def pat_home(request,pk):
    return render(request,'panacea_app/patienthome.html')
