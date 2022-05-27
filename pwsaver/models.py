from django.db import models
from django.contrib.auth.models import User

class Credential(models.Model):

    account_type = models.CharField(max_length=100,blank=True,null=True)
    username = models.CharField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.account_type