from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registrationform
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.

def login(request):
    return render(request,'login/login.html')

def signup(request):  
        return render(request,'registration/register.html')
def register(request):
        context={}
        Firstname=request.POST['firstname']
        Lastname = request.POST['lastname']
        Email = request.POST['email']
        Gender = request.POST['gender']
        Course = request.POST['course']
        Batch= request.POST['batch']
        obj = Registrationform.objects.create(firstname=Firstname,lastname=Lastname,email=Email,gender=Gender,course=Course,batch=Batch)
        obj.save()
        #messages.success(request,'account is registered',Firstname)
        send_mail('admin','hello world','kalyanikuppa1107@gmail.com',['tvsaiteja1661@gmail.com'])

        return redirect('adminform')


def loginuser(request):
        username=request.POST['username']
        password=request.POST['pwd']
        obj=Registrationform.objects.filter(password=password, email=username)
        if len(obj)!= False:
            print(obj)
            return render(request,'login/homepage.html')
        else:
             return render(request,'login/login.html')
    
def adminform(request):
        context={}
        data=Registrationform.objects.all()
        context['words']=data
     
        return render(request,'registration/adminpage.html',context)


def create_user(request):
        user=User.objects.create_user(username='prasad',email='prasad12@gmail.com')
        user.save()
        return HttpResponse('data saved')


        



