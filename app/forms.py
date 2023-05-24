from django import forms
from .models import CustomUser, EmployeeDetail
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
		

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = EmployeeDetail
		fields = ['emp_name', 'emp_role', 'emp_code', 'salary', 'gender']