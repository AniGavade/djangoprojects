from android.models import BwksStudents
from rest_framework import serializers

class apiserializer(serializers.ModelSerializer):
    class Meta:
        model=BwksStudents
        fields="__all__"
        