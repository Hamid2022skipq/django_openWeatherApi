from django.urls import path
from . import views
urlpatterns = [
# path('',views.signup),
# path('dashboard/',views.dashboard),
# path('/login',views.login),
path('',views.sign_up),
]