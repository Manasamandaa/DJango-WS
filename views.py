from django.shortcuts import render
from django.http import HttpResponse
from .models import student_data
def home(request):
    mymembers=student_data.objects.all()
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        student_data.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender
        )
        return HttpResponse("Data Added Successfully<a href='/home'>Go back")
    return render(request,'first.html',{'mymembers':mymembers})

