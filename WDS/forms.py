from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
'''
ssn_number = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    marital_status = models.CharField(max_length=1)
    i_type = models.CharField(max_length=1)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=5)
    '''

class houseform(forms.ModelForm):
	class Meta:
		model=Houses
		fields="__all__"
class customerform(forms.ModelForm):
	class Meta:
		model=Customer
		fields="__all__"
class driverform(forms.ModelForm):
	class Meta:
		model=Driver
		fields="__all__"
class hprform(forms.ModelForm):
	class Meta:
		model=HousePremium
		fields="__all__"
class invoiceform(forms.ModelForm):
	class Meta:
		model=Invoice
		fields="__all__"
class paymentform(forms.ModelForm):
	class Meta:
		model=Payment
		fields="__all__"
class policyform(forms.ModelForm):
	class Meta:
		model=Policy
		fields="__all__"
class vehicleform(forms.ModelForm):
	class Meta:
		model=Vehicle
		fields="__all__"



'''
class houseform(forms.ModelForm):
	class Meta:
		model=Houses
		fields=["purchase_date","area","house_type"]
class customerform(forms.ModelForm):
	class Meta:
		model=Customer
		fields=["ssn_number","first_name","last_name","gender","marital_status","i_type",
		"mobile_number","email_id","street","city","state","zip_code"]
class driverform(forms.ModelForm):
	class Meta:
		model=Driver
		fields=["liscense_num","first_name","last_name","birth_date","vehicle_vin"]
class hprform(forms.ModelForm):
	class Meta:
		model=HousePremium
		fields=["afn","hss","swimming_pool","basement"]
class invoiceform(forms.ModelForm):
	class Meta:
		model=Invoice
		fields=["due_date","amount"]
class paymentform(forms.ModelForm):
	class Meta:
		model=Payment
		fields=["payment_date","method","installment_amount"]
class policyform(forms.ModelForm):
	class Meta:
		model=Policy
		fields=["start_date","end_date","insurance_status"]
class vehicleform(forms.ModelForm):
	class Meta:
		model=Vehicle
		fields=["vehicle_make","vehicle_model","vehicle_status","vehicle_year","premium_amount"]
'''