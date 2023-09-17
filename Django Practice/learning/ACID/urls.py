from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('atomic/', views.atomicity)
]
class TransferView(GenericAPIView):
    def post(self,request,*args,**kwargs):
        pass