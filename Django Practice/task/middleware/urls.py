from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('log_out/',views.log_out,name='log_out'),
]