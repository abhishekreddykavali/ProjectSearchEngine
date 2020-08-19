from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Employee
from .serializers import EmployeeSerializers
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view



@login_required(login_url = "login/")
def searchfunction(request):
    if request.method=='POST':
        key = request.POST['query']
        
        pkObjs = Employee.objects.filter(name__contains=key)
        if pkObjs:
            return render(request,'app1/searchresult.html',{'obj':pkObjs})

        pkObjs = Employee.objects.filter(designation__contains=key)
        if pkObjs:
            return render(request,'app1/searchresult.html',{'obj':pkObjs})

        pkObjs = Employee.objects.filter(salary__contains=key)
        if pkObjs:
            return render(request,'app1/searchresult.html',{'obj':pkObjs})

        pkObjs = Employee.objects.filter(doj__contains=key)

        if pkObjs:
            return render(request,'app1/searchresult.html',{'obj':pkObjs})
        
        return redirect('search')
    else:
        return render(request,'app1/search.html')


@api_view(['GET'])
def specificapilist(request,doj):
    if request.method == 'GET':
        objs = Employee.objects.filter(doj__contains=doj)
        serializer = EmployeeSerializers(objs, many=True)
        return JsonResponse(serializer.data, safe=False)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                
                #Sending mail
                subject = 'Conformation mail'
                message = 'Welcome to our page, Thankyou for getting registered in our site'
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail(subject, message, from_email, to_list, fail_silently = False)
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


