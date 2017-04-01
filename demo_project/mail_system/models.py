from django.db import models
from django.contrib.auth.models import User


class Mail(models.Model):
    subject = models.CharField(max_length = 256)
    content = models.CharField(max_length = 4096)
    is_spam = models.BooleanField(default = False)

    class Meta:
        managed = True     
        app_label = 'mail_system' 

    def __str__(self):
        return ('\n' + ' ID: '+ str(self.id) +' Subject: ' + self.subject + ' Content: ' + self.content + ' Spam: ' + str(self.is_spam));

class User_Mail(models.Model):
    
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'sender_id')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'receiver_id')
    mail = models.ForeignKey(Mail, on_delete = models.CASCADE)
    is_read = models.BooleanField(default = False)
    
    class Meta:
        managed = True      
        app_label = 'mail_system'

    def __str__(self):
        return ('\n'+ ' ID: '+ str(self.id) + ' From: ' + self.sender.user.username+' To: '+ self.receiver.user.username+ ' Mail ID: ' + str(self.mail.id)); 

class Relation(models.Model):
    
    from_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'from_user_id')
    to_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'to_user_id')
    is_spam = models.BooleanField(default = False)
    
    class Meta:
        unique_together = ('from_user', 'to_user',)
        managed = True      
        app_label = 'mail_system' 

    def __str__(self):
        return ('\n'+ ' ID: '+ str(self.id) + ' From: ' + self.from_user.user.username+' To: '+ self.to_user.user.username + ' Spam: ' + str(self.is_spam));



