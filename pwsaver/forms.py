from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(max_length=20)

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

    
    def __init__(self, *args,**kwargs):

        super(RegisterForm,self).__init__(*args, **kwargs)
        
        # self.fields['username'].required = False
        # self.fields['password1'].required = False
        # self.fields['password2'].required = False
