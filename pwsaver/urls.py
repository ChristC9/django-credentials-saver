from django.urls import path
from .views import *
from django.contrib.auth.views import (PasswordResetView,PasswordResetDoneView,
PasswordResetConfirmView,PasswordResetCompleteView)


## TODO: Add urls for the views

urlpatterns = [
    path('',createCred,name='createCred'),
    path('get/',credenialList,name='credenialList'),
    path('login/',userlogin,name='user-login'),
    path('logout/',userlogout,name='user-logout'),
    path('register/',userregister,name='user-register'),
    path('pw/reset/',PasswordResetView.as_view(template_name='pwsaver/password_reset.html'),name='password_reset'),
    path('pw/reset/done/',PasswordResetDoneView.as_view(template_name='pwsaver/password_reset_done.html'),name='password_reset_done'),
    path('pw/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='pwsaver/password_reset_confirm.html'),name='password_reset_confirm'),
    path('pw/reset/complete/',PasswordResetCompleteView.as_view(template_name='pwsaver/password_reset_complete.html'),name='password_reset_complete'),
]