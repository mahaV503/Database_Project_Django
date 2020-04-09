from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
	email=forms.EmailField() #default is true we can make optional required=False

	class Meta:
		model=User
		fields=['username','email','password','password2']