from django.db import models

# Create your models here.
class service(models.Model):
    name=models.CharField(max_length=50)
    # title=models.CharField(max_length=50)
    # des=models.TextField()
    email=models.EmailField(null=True,blank=True)
    age=models.IntegerField(default=18)
    fee=models.IntegerField(default=2000)
