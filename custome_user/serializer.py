from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    print("customer serializer is working ----------------->")
    class Meta:
        model = CustomUser
        fields = '__all__'