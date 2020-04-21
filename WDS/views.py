from django.shortcuts import render
from django.http import HttpResponse
from .models import*
#List of dictionaries with two dummy posts
from django.shortcuts import redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *


def customercreate(request):
    cform=customerform(request.POST or None)
    if cform.is_valid():
        cform.save()
    context={
    'form':cform
    }
    return render(request,"WDS/signup.html",context)
#signup.html
def drivercreate(request):
    dform=driverform(request.POST or None)
    if dform.is_valid():
        dform.save()
        drivername=form.cleaned_data.get('first_name') #this is dictionary 
        messages.success(request,f'Account created for {drivername}')
        #return redirect('WDS-home')
         
    context={
    'form':dform
    }
    return render(request,"WDS/driver.html",context)
#driver.html
def hpcreate(request):
    hpform=hprform(request.POST or None)
    if hpform.is_valid():
        hpform.save()
        #drivername=form.cleaned_data.get('first_name') #this is dictionary 
        #messages.success(request,f'Account created for {drivername}')
        #return redirect('WDS-home')
         
    context={
    'form':hpform
    }
    return render(request,"WDS/homepremium.html",context)
#homepremium.html
def invoicecreate(request):
    iform=invoiceform(request.POST or None)
    if iform.is_valid():
        iform.save()
        #drivername=form.cleaned_data.get('first_name') #this is dictionary 
        #messages.success(request,f'Account created for {drivername}')
        #return redirect('WDS-home')
         
    context={
    'form':iform
    }
    return render(request,"WDS/invoice.html",context)
#invoice.html
def paymentcreate(request):
    pform=paymentform(request.POST or None)
    if pform.is_valid():
        pform.save()
        #drivername=form.cleaned_data.get('first_name') #this is dictionary 
        #messages.success(request,f'Account created for {drivername}')
        #return redirect('WDS-home')
         
    context={
    'form':pform
    }
    return render(request,"WDS/payment.html",context)
#payment.html
def vehiclecreate(request):
    vform=vehicleform(request.POST or None)
    if vform.is_valid():
        vform.save()
        #drivername=form.cleaned_data.get('first_name') #this is dictionary 
        #messages.success(request,f'Account created for {drivername}')
        #return redirect('WDS-home')
         
    context={
    'form':vform
    }
    return render(request,"WDS/vehicle.html",context)
#vehicle.html
def housecreate(request):
    hform=houseform(request.POST or None)
    if hform.is_valid():
        hform.save()
        #drivername=form.cleaned_data.get('first_name') #this is dictionary 
        #messages.success(request,f'Account created for {drivername}')
        #return redirect('WDS-home')
         
    context={
    'form':hform
    }
    return render(request,"WDS/house.html",context)
#house.html
def policycreate(request):
    pform=policyform(request.POST or None)
    if pform.is_valid():
        pform.save()
        #drivername=form.cleaned_data.get('first_name') #this is dictionary 
        #messages.success(request,f'Account created for {drivername}')
        #return redirect('WDS-home')
         
    context={
    'form':pform
    }
    return render(request,"WDS/policy.html",context)
#policy.html

def login(request):
    return render(request,'WDS/login.html')

'''
def homeview(request):
	view1={
	'cstmrkey': Customer.objects.all()
	}
	#return HttpResponse('<h1> Welcome to we do secure <h1>')
	return render(request, 'WDS/aHomePage/Home.html',view1)
'''

def signup(request):
    if request.method =='POST':
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') #this is dictionary 
            messages.success(request,f'Account created for {username}')
            return redirect('WDS-home')
    else:
        form =UserRegForm()
    return render(request,'WDS/signup.html',{'form':form})

def home(request):
    return render(request,'WDS/home.html')

def about(request):
    return render(request,'WDS/about.html')

def emplogin(request):
    return render(request,'/admin')
