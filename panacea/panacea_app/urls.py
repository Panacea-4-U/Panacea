from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='web-home'),
    path('patient/<int:pk>/',views.pat_home,name='pat-home'),
    path('landing', views.landingpage,name='landing-page'),
    path('login-register', views.login_register,name='login-register'),
    path('about us',views.about_us,name='about us'),
    path('contact_us',views.contact_us,name='contact us'),
    path('doctor-details', views.doctordetails,name='doctordetails'),
    path('patient-details', views.patientdetails,name='patientdetails'),
    path('db_check/',views.check, name='check')
]
