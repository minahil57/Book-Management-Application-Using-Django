from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .serializers import AddBookSerializer, GetBookSerializer, UpdateBookSerializer
from .models import Book
class AddBookView(viewsets.ViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        
        serializer = AddBookSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Book added successfully"
            })
        else:
            return Response({
                "status": False,
                "message": serializer.errors
            })


class GetBookList(viewsets.ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = GetBookSerializer(books, many=True)
        return Response({
            "status": True,
            "data": serializer.data
        })

class UpdateBookView(viewsets.ViewSet):
    def update(self, request, pk):
        book = Book.objects.get(id=pk)
        data = request.data
        serializer = UpdateBookSerializer(instance=book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Book updated successfully"
            })
        else:
            return Response({
                "status": False,
                "message": serializer.errors
            })
    
    def partial_update(self, request, pk):
        book = Book.objects.get(id=pk)
        data = request.data
        serializer = UpdateBookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Book updated successfully"
            })
        else:
            return Response({
                "status": False,
                "message": serializer.errors
            })


class DeleteBookView(viewsets.ViewSet):
    def destroy(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response({
            "status": True,
            "message": "Book deleted successfully"
        })



class GetBookView(viewsets.ViewSet):
    def retrieve(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = GetBookSerializer(book)
        return Response({
            "status": True,
            "data": serializer.data
        })