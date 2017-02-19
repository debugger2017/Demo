from django import forms

from django.contrib.auth.models import User
from mail_system.models import RegisteredUsers, Mail

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())	
	class Meta:
		model = User	
		fields = ('username','email','password')

class RegisteredUsersForm(forms.ModelForm):
	class Meta:
		model = RegisteredUsers
		fields = ('mobile','city')

from mail_system.models import Mail

class MailForm(forms.ModelForm):
    receiver = forms.CharField(label = "To")
    
    class Meta:
        model = Mail
        fields = ('content','subject')