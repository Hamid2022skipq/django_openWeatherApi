from django.db import models
from django.contrib.auth.models import User
class Request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    view = models.CharField(max_length=250) # this could also represent a URL
    visits = models.PositiveIntegerField()