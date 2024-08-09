from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctor
from .forms import BookingForm
def index(request):
    return render(request,"index.html")
def about(request):
    return HttpResponse ("About us")
       
#def basecall(request):
#   dic_basecall={
#      'basecall':Department.objects.all()
# }
# return render(request,"basecall.html")
def department(request):
    dic_dept={
        'dept':Department.objects.all()
    }
    return render(request,"department.html",dic_dept)
def doctor(request):
    dic_doc={
        'doc':Doctor.objects.all()
    }
    return render(request,"doctor.html",dic_doc)
def booking(request):
    if request.method=="POST":
       form=BookingForm(request.POST)
       if form.is_valid():
          form.save()
    else:
       form=BookingForm()
       dic_form={
          'form':form
    }
    return render(request,"booking.html",dic_form)

# Create your views here.
