from django.db import models

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



