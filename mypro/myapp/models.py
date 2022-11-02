from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.BigIntegerField(null=False)
    password=models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
    
# class students(models.Model):
#     number=models.OneToOneField(users,on_delete=models.CASCADE,primary_key=True)
#     address=models.CharField(max_length=120)

#     def __str__(self):
#         return self.address 
