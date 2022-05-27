from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Credential


@login_required
def createCred(request):
    
    if request.method == 'POST':
            
        data = request.POST
        account_type = data['account_type']
        username = data['username']
        password = data['password']

        Credential.objects.create(
                account_type = account_type,
                username = username,
                password = password
            )
        return redirect('/get/')
    return render(request,'pwsaver/credentialsform.html')

@login_required
def credenialList(request):

    credential = Credential.objects.all()
    return render(request,'pwsaver/credentialsList.html',{'credentials':credential})


def userlogin(request):

    message = None
    if request.method == 'POST':

        data = request.POST
        username = data['username']
        password = data['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            message = f'You have been logged in'
            return redirect('/')
        else:
            message = 'username or password incorrect Logged in failed'   

    return render(request,'pwsaver/login.html',{'message':message})

def userlogout(request):

    logout(request)
    return redirect('/login/')
