from django.db import models

# Create your models here.

class UserSignUp(models.Model):
    names = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False)
    password = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.names