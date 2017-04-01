from django.contrib import admin
from django.contrib.auth.models import User
from mail_system.models import Mail, Mail_Information,Spammed_Sender

admin.site.register(Mail)
admin.site.register(Spammed_Sender)