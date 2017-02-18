from django import forms
from mail_system.models.py import Mail

class MailForm(forms.ModelForm) :
    reciever = forms.CharField(widget = forms.IextInput())
    subject = forms.CharField(widget = forms.TextInput())
    content = froms.CharField(widget = forms.TextInput(attrs = {'class':'special'}))
