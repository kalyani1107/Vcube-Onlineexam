from django.db import models

# Create your models here.

class Registrationform(models.Model):
    firstname=models.CharField(max_length=40,null=False)
    lastname=models.CharField(max_length=40,null=False)
    email=models.EmailField(max_length=80,null=False,unique=True)
    gender=models.CharField(max_length=30,null=False)
    course=models.CharField(max_length=40,null=False)
    batch=models.CharField(max_length=40,null=False)
    
    
    def __str__(self):
        return (self.firstname)
