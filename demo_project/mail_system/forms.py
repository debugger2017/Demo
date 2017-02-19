from django import forms

from django.contrib.auth.models import User
from mail_system.models import RegisteredUsers, UserMails

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
    receiver = forms.CharField(label = 'To', error_messages = {'required':'please enter valid receiver'})
    class Meta:
    	model = Mail
    	fields = ('content','subject')

    def	clean(self):
        cleaned_data  = self.cleaned_data
        subject = cleaned_data.get('subject')
        receiver = cleaned_data.get('receiver')
        #print(subject, receiver)
        #if( len(subject) <= 0 ):
         #   raise forms.ValidationError("Subject can not be blank")
        #if(receiver.length <= 0):
         #   raise forms.ValidationError("Receiver feild should not be blank")



