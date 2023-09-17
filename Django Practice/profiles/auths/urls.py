from django.urls import path
from . import views
urlpatterns = [
path('',views.sign_up,name='signup'),
path('login/',views.log_in,name='login'),
path('dashboard/',views.dashboard),
path('log_out/',views.log_out,name='log_out'),
path('change_pass/',views.change_pass,name='change_pass'),
path('change_pass1/',views.change_pass1,name='change_pass1'),
path('userprofile/<int:id>',views.userprofile,name='userprofile'),
]