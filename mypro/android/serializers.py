from rest_framework import serializers
from .models import BwksStudents
class BwksStudentSer(serializers.ModelSerializer):
    class Meta:
        model=BwksStudents
        fields="__all__"
        