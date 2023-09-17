from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signup(UserCreationForm):
    password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={'email':"Email",'username':'Username','first_name':'First Name','last_name':'Last Name'}

# normal user profile 
class EditUserChangeForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email'}

# Admin user profile
class EditAdminChangeForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login','is_active','is_staff','is_superuser']
        labels={'email':'Email'}