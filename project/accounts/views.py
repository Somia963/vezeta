from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

# accounts/views.py
def doctors_list(request):
    doctors = User.objects.all()
    
    return render(request , 'user/doctors_list.html' , {
        'doctors'  : doctors,
    })
def doctors_details(request , slug):
    doctors_details = Profile.object.get(slug =slug)
    
    return render(request , 'user/doctors_details.html',{
        'doctor_detail' : doctors_details,
    })

