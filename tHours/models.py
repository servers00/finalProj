from django.db import models
from django.contrib.auth.models import User

class totalHours(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=255, null=True)
	goal = models.CharField(max_length=255, null=True)
	trackMethod = models.CharField(max_length=255, null=True)
	hoursWorked = models.IntegerField(null=True)
	#methods = models.CharField(max_length=255)
	#reason = models.CharField(max_length=255)
	#completionDate = models.IntegerField(default="false")