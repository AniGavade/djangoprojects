from android.models import BwksStudents
from android.api.serializers import apiserializer
from rest_framework import viewsets

class CBVclassviewset(viewsets.ModelViewSet):
    queryset=BwksStudents.objects.all()
    serializer_class=apiserializer  