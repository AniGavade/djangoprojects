from django.shortcuts import render

# Create your views here.
from .serializers import BwksStudentSer
from .models import BwksStudents
from rest_framework import viewsets

class BwksStuViewset(viewsets.ModelViewSet):
    queryset=BwksStudents.objects.all()
    serializer_class=BwksStudentSer
