from rest_framework import serializers
from .models import Review
from book_management.models import Book

class AddReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        if "review" in data:        
            if len(data["review"]) < 10:
                raise serializers.ValidationError(
                    "Review must be at least 10 characters"
                )
        return data

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["review", "rating"]

    def validate(self, data):
        if "review" in data:        
            if len(data["review"]) < 10:
                raise serializers.ValidationError(
                    "Review must be at least 10 characters"
                )
        return data



class GetReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review  
        fields = '__all__'

    def validate(self, data):
        return data


class DeleteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id']

    def validate(self, data):
        return data
