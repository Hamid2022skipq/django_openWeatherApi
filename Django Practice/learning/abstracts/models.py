from django.db import models

# Create your models here.
class CommmonInfo(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True
class Student(CommmonInfo):
    fee=models.IntegerField()
    date=None
class Teacher(CommmonInfo):
    salary=models.IntegerField()
class Contractor(CommmonInfo):
    date=models.DateTimeField()
    payment=models.IntegerField()
