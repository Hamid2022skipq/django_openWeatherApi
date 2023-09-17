from django.urls import path
from . import views
urlpatterns = [
    path('',views.hello),
    path('set/',views.setcookies),
    path('get/',views.getcookies),
    path('del/',views.delcookies),
]