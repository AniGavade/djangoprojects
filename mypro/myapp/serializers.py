from rest_framework import serializers
from .models import users

class userserializer(serializers.Serializer):
    name=serializers.CharField(max_length=120)
    email=serializers.CharField(max_length=120)
    phone=serializers.IntegerField()
    password=serializers.CharField(max_length=120)
    def create(self, validated_data):
        return users.objects.create(**validated_data)