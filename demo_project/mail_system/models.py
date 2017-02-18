from django.db import models

# Create your models here.
class Mail(models.model):
    subject = models.CharField(max_length = 128)
    content = models.CharField(max_length = 4096)
    is_spam = models.BooleanField(defualt = FALSE)
    is_read = models.BooleanField(default = FALSE)
    timestamp = models.DateTimeField(auto_now_add = TRUE,unique = TRUE)
    
    def __str__(self):
        return self.subject;



