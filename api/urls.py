from django.urls import path
from .views import *

urlpatterns = [
  
    path('',api,name="home")
    # path('contry_info/',api)
]