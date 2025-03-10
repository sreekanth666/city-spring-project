from .models import *
from rest_framework import serializers



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        """
        Optional: Add custom validation if you want to check credentials here
        instead of in the view.
        """
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")
        
        return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class AdminViewUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','phone_number','email']

