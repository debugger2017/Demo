from django import forms
from mail_system.models import Mail, RegisteredUsers
from django.contrib.auth.models import User 

class UserForm(forms.ModelForm):
	password = forms.CharField(label="",widget = forms.PasswordInput())
	username = forms.CharField(label="",widget = forms.TextInput())
	email = forms.CharField(label="",widget = forms.TextInput())	
	class Meta:
		model = User	
		fields = ('username','email','password')

class RegisteredUsersForm(forms.ModelForm):
	mobile = forms.CharField(label="",widget = forms.TextInput())
	city = forms.CharField(label="",widget = forms.TextInput())
	class Meta:
		model = RegisteredUsers
		fields = ('mobile','city')

class MailForm(forms.ModelForm):
    class Meta:
    	model = Mail
    	fields = ('content','subject')	
