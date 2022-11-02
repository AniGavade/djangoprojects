from django.db import models

# Create your models here.
class BwksStudents(models.Model):
    name=models.CharField(max_length=100)
    batch=models.CharField(max_length=100)
    salary=models.IntegerField()
    def __str__(self):
        return self.name
        