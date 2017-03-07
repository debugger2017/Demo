from django.db import models
from django.contrib.auth.models import User

class RegisteredUsers(models.Model):
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length = 10)
    city = models.CharField(max_length = 10)

    class Meta:
        managed = True      # add this
        app_label = 'mail_system' 

    def __str__(self):
        return self.user.username

# Create your models here.
class Mail(models.Model):
    subject = models.CharField(max_length = 256)
    content = models.CharField(max_length = 4096)
    is_spam = models.BooleanField(default = False)
    is_read = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True,unique = True)

    class Meta:
        managed = True      # add this
        app_label = 'mail_system' 

    def __str__(self):
        return self.subject;

class UserMails(models.Model):
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "sender_id")
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "receiver_id")
    mail = models.ForeignKey(Mail, on_delete = models.CASCADE)

    class Meta:
        managed = True      # add this
        app_label = 'mail_system' 


