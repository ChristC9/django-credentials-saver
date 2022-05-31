from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import RegisterForm
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
                password = password,
                user = request.user
            )
        return redirect('/get/')
    return render(request,'pwsaver/credentialsform.html')

@login_required
def credenialList(request):

    credential = Credential.objects.filter(user=request.user)
    return render(request,'pwsaver/credentialsList.html',{'credentials':credential})


def userlogin(request):

    if request.method == 'POST':

        data = request.POST
        username = data['username']
        password = data['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid username or password',extra_tags='alert')

    return render(request,'pwsaver/login.html')

def userlogout(request):

    logout(request)
    return redirect('/login/')


def userregister(request):

    data = request.POST
    form = RegisterForm()

    if request.method == 'POST':
        
        form = RegisterForm(data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account, {username} is created successfully.')
            return redirect('/login/')
            
    return render(request,'pwsaver/register.html',{'form':form})
