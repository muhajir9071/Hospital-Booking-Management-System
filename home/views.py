from django.shortcuts import render
from django.http import HttpResponse
from  .forms import BookingForm
from . models import Department,Doctors
# Create your views here.
def index(request):
    numbers={
        'num1':[1,2,3,4,5,6,7,8,9,10]

    }

    return render(request,'index.html',numbers)
def about(request):
    return render(request,'about.html')
def booking(request):
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)