from django import forms
from django.contrib.auth.models import User 
from mail_system.models import Mail

class UserForm(forms.ModelForm):
	password = forms.CharField(label="",widget = forms.PasswordInput(attrs = {'placeholder': 'Password'}))
	username = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'Username'}))
	email = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'Email'}))	
	class Meta:
		model = User	
		fields = ('username','email','password')

class MailForm(forms.ModelForm):
    receiver = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'To'})) 
    content = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'Content'}))    
    subject = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'Subject'}))
    class Meta:
        model = Mail
        fields = ('subject','content')
