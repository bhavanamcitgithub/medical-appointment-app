
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('appoinemnet.html', views.appointment,name="appointment"),
  


]
