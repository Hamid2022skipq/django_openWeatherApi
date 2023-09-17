from django.db import models
from django.contrib.auth.models import User
import datetime
class Page(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    # user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    user=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True,limit_choices_to={'is_staff':True})
    name=models.CharField(max_length=70)
    cattogare=models.CharField(max_length=70)
    publish_date=models.DateField(default=datetime.date.today() )