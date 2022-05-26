from django.db import models

class Credential(models.Model):

    account_type = models.CharField(max_length=100,blank=True,null=True)
    username = models.CharField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.account_type