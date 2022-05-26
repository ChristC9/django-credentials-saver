from django.shortcuts import render,redirect
from .models import Credential

def createCred(request):
    if request.method == 'POST':
        
        data = request.POST
        account_type = data['account_type']
        username = data['username']
        password = data['password']

        credentials = Credential.objects.create(
            account_type = account_type,
            username = username,
            password = password
        )
        return redirect('/get/')
    return render(request,'pwsaver/credentialsform.html')


def credenialList(request):

    credential = Credential.objects.all()
    return render(request,'pwsaver/credentialsList.html',{'credentials':credential})