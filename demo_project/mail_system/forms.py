from django import forms
from mail_system.models import Mail

class MailForm(forms.ModelForm):
    class Meta:
    	model = Mail
    	fields = ('content','subject')	
