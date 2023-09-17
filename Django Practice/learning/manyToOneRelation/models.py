from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    publish_date=models.DateField(default=timezone.now())

class Book(models.Model):
    user=models.ManyToManyField(User)
    title=models.CharField(max_length=70)
    pages=models.CharField(max_length=70)
    # intership=models.BooleanField()
    publish_date=models.DateField(default=timezone.now())
    def Users(self):
        return " , ".join([str(x).capitalize() for x in self.user.all()])

