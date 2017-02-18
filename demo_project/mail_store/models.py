from django.db import models

# Create your models here.
class Mail(models.model):
    subject = models.CharField(max_length=128)
    content = models.CharField(max_length=4096)
    is_spam = models.BooleanField()
    is_read = models.BooleanField()
    timestamp = models.DateTimeField(unique = TRUE)



