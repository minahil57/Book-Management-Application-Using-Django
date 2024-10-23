from rest_framework import serializers
from .models import Book


class AddBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):
        if "title" in data:
            if len(data["title"]) < 5:
                raise serializers.ValidationError(
                    "Title must be at least 5 characters"
                )
        if "author" in data:
            if len(data["author"]) < 5:
                raise serializers.ValidationError(
                    "Author must be at least 5 characters"
                )
        if "description" in data:
            if len(data["description"]) < 10:
                raise serializers.ValidationError(
                    "Description must be at least 10 characters"
                )
                
        return data


class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "bookImage"]

    def validate(self, data):
        if "title" in data:
            if len(data["title"]) < 5:
                raise serializers.ValidationError(
                    "Title must be at least 5 characters"
                )
        if "author" in data:
            if len(data["author"]) < 5:
                raise serializers.ValidationError(
                    "Author must be at least 5 characters"
                )
        if "description" in data:
            if len(data["description"]) < 10:
                raise serializers.ValidationError(
                    "Description must be at least 10 characters"
                )
        return data


class DeleteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    



class GetBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
      

