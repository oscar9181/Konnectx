from django.urls import path,include
from django.contrib.auth import views 
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name="landingPage"),
    path('',views.home,name='home'),
    path('',views.register,name ='register'),
    path('artist_register/',views.artist_register.as_view(),name='artist_register'),
    path('distributor_register/',views.distributor_register.as_view(),name='distributor_register'),
 

]