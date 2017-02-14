from django.db import models
from django.contrib.auth.models import User

class RegisteredUsers(models.Model):
	user = models.OneToOneField(User)
	mobile = models.CharField(max_length = 10)
	city = models.CharField(max_length = 10)

	def __str__(self):
		return self.user.username