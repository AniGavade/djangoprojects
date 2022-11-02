from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Singer,Song
from .serializers import SingerSerializer,SongSerializer

class Singerviewset(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer

class Songviewset(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer