from django.db import models

# Create your models here.

#various techniques to model inheritance in django:
# 1) abstract base class model inheritance: used when u want to parent class holds info. that u dont want to write on each child class 
# 2) multi table model inheritance:used when u are subclassing an existing model to have its own table in the db.
# 3) proxy model inheritance: used when u want to retain the model field while altering the python level functioning of the model

# 1) abstract base class model inheritance:
class parent(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)                 #parent class whose hold info about the child class 
    class Meta:
        abstract=True
class clsrooom(parent):
    address=models.CharField(max_length =100)               #child class holds info about the parent class 

# 2) multi table model inheritance:
class Examcenter(models.Model):
    sname=models.CharField(max_length=90)
    sroll=models.IntegerField()
class students(Examcenter):
    name=models.CharField(max_length=90)
    seat=models.IntegerField()

# 3)proxy model inheritance techiniques
# class proxycls(Examcenter):
#     pname=models.CharField(max_length=90)
#     proll=models.IntegerField()
#     class Meta:
#         proxy=True

