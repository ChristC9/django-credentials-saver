from django.urls import path
from .views import *


## TODO: Add urls for the views

urlpatterns = [
    path('',createCred,name='createCred'),
    path('get/',credenialList,name='credenialList'),
]