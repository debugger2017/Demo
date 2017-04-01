from django.contrib import admin
from django.contrib.auth.models import User
from mail_system.models import Mail,User_Mail,Relation

admin.site.register(Mail)
admin.site.register(Relation)