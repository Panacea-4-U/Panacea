from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='web-home'),
    path('landing', views.landingpage,name='landing-page'),
    path('login-register', views.login_register,name='login-register'),
    path('doctor-details', views.doctordetails,name='doctordetails'),
    path('patient-details', views.patientdetails,name='patientdetails'),
    path('db_check/',views.check, name='check')
]
