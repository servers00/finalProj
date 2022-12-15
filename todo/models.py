from django.db import models
from django.contrib.auth.models import User

class TodoItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TodoItem = models.CharField(max_length=100)
    descriprion = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
