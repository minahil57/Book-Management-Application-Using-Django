from rest_framework import serializers
from .models import User


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')

    def validate(self, data):
        if "password" in data:
            if len(data["password"]) < 8:
                raise serializers.ValidationError(
                    "Password must be at least 8 characters"        
                )
            if not any(char.isdigit() for char in data["password"]):
                raise serializers.ValidationError(
                    "Password must contain at least one number"
                )
            if not any(char.isupper() for char in data["password"]):
                raise serializers.ValidationError(
                    "Password must contain at least one uppercase letter"
                )
            if not any(char.islower() for char in data["password"]):
                raise serializers.ValidationError(
                    "Password must contain at least one lowercase letter"
                )
            if not any(char in "!@#$%^&*()" for char in data["password"]):
                raise serializers.ValidationError(
                    "Password must contain at least one special character"
                )
    
        print("data: ", data)
        return data

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)
