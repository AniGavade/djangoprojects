from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.BigIntegerField(null=False)
    password=models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
class Mobile(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    ankit=models.Manager()
    def __str__(self):
        return self.name 
        