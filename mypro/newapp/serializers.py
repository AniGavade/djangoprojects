from rest_framework import serializers
from .models import Mobile, users

class userserializer(serializers.Serializer):
    name=serializers.CharField(max_length=120)
    email=serializers.CharField(max_length=120)
    phone=serializers.IntegerField()
    password=serializers.CharField(max_length=120)
    def create(self, validated_data):
        return users.objects.create(**validated_data)
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get("email",instance.email)
        instance.phone=validated_data.get("phone",instance.phone)
        instance.password=validated_data.get('password',instance.password)
        instance.save()
        return instance
    def validate_phone(self,value):
        if value>1000:
            raise serializers.ValidationError("please enter valid number")
        return value
class modelserializer(serializers.ModelSerializer):
    class Meta:
        model = users 
        fields="__all__"

class mobileserializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile 
        fields="__all__"

